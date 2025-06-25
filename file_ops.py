import json

def load_failed_attempts():
    try:
        with open("failed_attempts_file.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_failed_attempts(timestamps):
    with open("failed_attempts_file.json", "w") as f:
        json.dump(timestamps, f)
