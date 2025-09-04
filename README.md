# 🔐 Webhook Firewall

A smart, CLI + Flask-based utility that acts as a middleware firewall for webhook events.  
It captures, logs, mocks, and lets you review incoming payloads from tools like GitHub, Stripe, and Slack — all locally, no dashboards.

---

### ✅ What It Does

- Logs webhook payloads to local files
- CLI tool to inspect recent activity
- Optional rule engine for allow/block by source
- Sends back mock responses for testing integrations

---

### 🧪 Quick Start

```bash
pip install -r requirements.txt
python app.py         # Start the Flask server
python cli.py         # View recent webhooks

📦 Folder Structure

app.py: Flask server for webhook ingestion

cli.py: Inspect and review logs

rules.yaml: Define allow/deny behavior

mock_responses/: Send fake payload replies

logs/: Saved webhook logs

Built by André Adeyemi
. MIT Licensed.

Ready to copy?  
✅ Hit **Create repository** now  
✅ Then paste these files via mobile GitHub editor or wait till you're on a desktop  
📩 Let me know when you're ready for the next enhancement (like AI filtering or Replit deploy).
