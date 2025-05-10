# app/monitor.py

import time
import threading
from app.websocket import manager
from app.utility import read_new_lines

LOG_FILE = "logs/sample.log"

def monitor_logs():
    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)  # Move cursor to end
        while True:
            new_lines = read_new_lines(f)
            if new_lines:
                for line in new_lines:
                    manager.broadcast(line.strip())
            time.sleep(1)  # Check every 1 second

def start_monitoring():
    t = threading.Thread(target=monitor_logs)
    t.daemon = True
    t.start()

def read_new_lines(file_obj):
    lines = []
    while True:
        line = file_obj.readline()
        if not line:
            break
        lines.append(line)
    return lines
