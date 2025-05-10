import time
import random
from datetime import datetime

def generate_logs():
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    messages = [
        "User logged in successfully",
        "File uploaded successfully",
        "An error occurred while processing request",
        "Database connection established",
        "Configuration file loaded",
        "New user registered",
        "Scheduled task completed",
        "Cache memory cleared",
        "Unauthorized login attempt detected",
        "Payment transaction completed"
    ]

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level = random.choice(log_levels)
        message = random.choice(messages)
        log_entry = f"[{timestamp}] [{level}] {message}\n"

        with open("logs/sample.log", "a") as log_file:
            log_file.write(log_entry)

        print(f"Generated log: {log_entry.strip()}")
        time.sleep(5)  # Sleep for 5 seconds before next log

if __name__ == "__main__":
    generate_logs()
