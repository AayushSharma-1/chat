import json
import os


def write_to_json(data, filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding='utf-8') as file:
            existing_data = json.load(file)
        # Check if the email already exists in the file
        if "email" in data:
            existing_emails = [
                entry["email"] for entry in existing_data if "email" in entry
            ]
            if data["email"] in existing_emails:
                return
        existing_data.append(data)
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(existing_data, file, indent=4)
    else:
        with open(filename, "w", encoding='utf-8') as file:
            json.dump([data], file, indent=4)

