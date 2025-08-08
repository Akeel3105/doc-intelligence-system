# logger.py
import csv
import os
from datetime import datetime

def save_to_csv(data: dict, filename="logs.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp"] + list(data.keys()))
        if not file_exists:
            writer.writeheader()
        data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow(data)
