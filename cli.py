import json

LOG_FILE = "logs/webhook_log.json"

def show_logs():
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            print(f"📜 Showing {len(lines)} webhook(s):\n")
            for line in lines[-5:]:
                data = json.loads(line)
                print(f"[{data['timestamp']}] Payload: {data['payload']}")
    except FileNotFoundError:
        print("⚠️ No logs found.")

if __name__ == "__main__":
    show_logs()
