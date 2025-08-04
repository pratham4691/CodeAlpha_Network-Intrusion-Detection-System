import subprocess
import time
import json
from pathlib import Path
from threading import Thread

SURICATA_CONFIG = "/etc/suricata/suricata.yaml"
INTERFACE = "eth0"  # Update as needed
EVE_JSON_PATH = "/var/log/suricata/eve.json"

def run_suricata():
    # Launch Suricata in a subprocess
    cmd = [
        "sudo", "suricata", "-c", SURICATA_CONFIG, "-i", INTERFACE
    ]
    print(f"Running Suricata with: {' '.join(cmd)}")
    subprocess.Popen(cmd)

def follow_eve_json(callback):
    # Monitor eve.json for new lines (alerts)
    path = Path(EVE_JSON_PATH)
    print(f"Monitoring {EVE_JSON_PATH} for alerts...")
    with path.open("r") as f:
        # Seek to end of file
        f.seek(0,2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            try:
                event = json.loads(line)
                callback(event)
            except Exception as e:
                print("Error parsing Suricata alert:", e)

def alert_callback(event):
    # Customize alert handling here
    if event.get("event_type") == "alert":
        alert = event['alert']
        print(f"[ALERT] {alert['signature']} | src: {event['src_ip']} dst: {event['dest_ip']}")
        # Optionally trigger response mechanisms, notifications, etc.

def main():
    # Start Suricata in a background thread
    Thread(target=run_suricata, daemon=True).start()
    # Start monitoring eve.json
    follow_eve_json(alert_callback)

if __name__ == "__main__":
    main()
