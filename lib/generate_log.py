from datetime import datetime
import os

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Data must be a list of log entries.")

    # STEP 2: Generate filename with today's date
    today_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today_str}.txt"

    # STEP 3: Write log entries to the file
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation
    print(f"Log written to {filename}")

    return filename

