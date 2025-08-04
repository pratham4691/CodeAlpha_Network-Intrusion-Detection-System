# Network Intrusion Detection System (NIDS) with Suricata

This project provides a Python-based interface to set up, monitor, and respond to network intrusions using [Suricata](https://suricata.io/), a powerful open-source network threat detection engine.

## Features

- **Automated Suricata Launch:** Starts Suricata with a specified config and interface.
- **Real-Time Alert Monitoring:** Continuously monitors Suricata's `eve.json` for intrusion alerts.
- **Custom Alert Handling:** Easily extend the alert callback to trigger notifications or automated responses.
- **Integration-Ready:** Can be connected to dashboards (e.g., Kibana, Grafana) for visualization.

## Requirements

- Python 3.6+
- Suricata installed and configured
- Sudo privileges to launch Suricata

## Quick Start

1. **Install Suricata:**  
   Follow [Suricata installation instructions](https://suricata.io/docs/) for your OS.

2. **Update the Python Script:**  
   - Set `INTERFACE` to your network interface (e.g., `eth0`, `enp0s3`).
   - Confirm the paths for `SURICATA_CONFIG` and `EVE_JSON_PATH`.

3. **Run the Script:**
   ```bash
   python3 network_ids_suricata.py
   ```

4. **View Alerts:**  
   Alerts will be printed to the console as they are detected. Customize the `alert_callback` function to integrate notifications or automate incident response.

## Example Output

```
[ALERT] ET MALWARE Possible Evasive SSH Scan | src: 192.168.1.10 dst: 192.168.1.100
```

## Customization

- **Alert Handling:**  
  Modify `alert_callback(event)` in `network_ids_suricata.py` to:
  - Send emails, Slack messages, or syslog alerts
  - Trigger scripts for automated blocking/quarantine
  - Log to external SIEM systems

- **Visualization:**  
  Send `eve.json` events to [ELK Stack](https://www.elastic.co/what-is/elk-stack) or similar tools for dashboards and analysis.

## Troubleshooting

- Ensure Suricata is properly installed and the config path is correct.
- Check permissions for reading `eve.json`.
- If you see no alerts, verify Suricata is receiving network traffic on your specified interface.

## References

- [Suricata Documentation](https://suricata.io/docs/)
- [Suricata Rules](https://rules.emergingthreats.net/)
- [Python subprocess module](https://docs.python.org/3/library/subprocess.html)

---

*This project is for educational and demonstration purposes. For production, ensure proper security hardening and monitoring.*
