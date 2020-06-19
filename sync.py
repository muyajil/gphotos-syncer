import subprocess
import requests
import time
import os

SYNC_COMMAND = [
    "gphotos-sync",
    "--omit-album-date",
    "--logfile",
    "/last_run_debug.log",
    "--log-level",
    "info",
    "--db-path",
    "/config",
    "--secret",
    "/client_secret.json"
    "/download"]

client_secret = os.environ.get('CLIENT_SECRET')
with open("/client_secret.json", "w") as f:
    f.write(client_secret)

def send_message_to_slack(message, markdown=True):
    data = {"text": message, "markdown": True}
    url = os.environ.get('SLACK_WEBHOOK')
    print(url)
    _ = requests.post(
        url,
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )

while True:
    try:
        result = subprocess.call(SYNC_COMMAND)
        result.check_return_code()
    except subprocess.CalledProcessError:
        send_message_to_slack('There was a problem with the Google Photos Sync')
    time.sleep(3600)