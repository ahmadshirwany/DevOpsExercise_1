from fastapi import FastAPI, Response
import requests
import subprocess
from datetime import datetime, timezone
import os
log_dir = "/vstorage"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "log.txt")

app = FastAPI()

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_s = float(f.readline().split()[0])
    uptime_h = int(uptime_s // 3600)
    freespace_in_kb = subprocess.run(['df', '-k'], capture_output=True, text=True)
    freespace_in_mb = int(freespace_in_kb.stdout.split('\n')[1].split()[3]) // 1024
    time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')
    return f"Service1 Uptime: {uptime_h} hours, Free Memory: {freespace_in_mb} MB, Time: {time}"

@app.get("/status")
def status():
    data1 = get_uptime()
    try:
        requests.post("http://storage:8003/log", data=data1)
    except requests.exceptions.RequestException as e:
        print(f"Error logging to storage: {e}")

    try:
        response = requests.get("http://service2:8002/status")
        data2 = response.text
    except Exception as e:
        data2 = f"ERROR: Service2 unreachable - {str(e)}"
    try:
        with open('/vstorage/log.txt', 'a') as f:
            f.write(f"{data1}\n\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")
    return Response(content=f"Response :{data1}\n{data2}", media_type="text/plain")

app.get("/log")
def log():
    try:
        response = requests.post("http://storage:8003/log")
        return Response(content=response.text, media_type="text/plain")
    except requests.exceptions.RequestException as e:
        return Response(content=f"Error logging to storage: {e}", media_type="text/plain")
    