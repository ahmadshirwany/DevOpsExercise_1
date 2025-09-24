from flask import Flask, request, Response
import os
from datetime import datetime
app = Flask(__name__)
dir = "/storage"
file = os.path.join(dir, "log.txt")
os.makedirs(dir, exist_ok=True)

@app.route("/log", methods=["POST"])
def add_log():
    data = request.get_data(as_text=True)
    if not data:
         return Response(f"No data provided", status=400)
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {data}\n"
        with open(file, "a") as f:
            f.write(log_entry)
        return Response(f"Logged", status=200)
    except Exception as e:
         return Response(f"Error line 21: {e}", status=500)

@app.route("/log", methods=["GET"])
def get_log():
    try:
        with open(file, "r") as f:
            logs = f.read()
        return Response(logs, mimetype="text/plain", status=200)
    except FileNotFoundError:
        return Response(f"No logs found", status=404)
    except Exception as e:
        return Response(f"Error: {e}", status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)
    
