import json

def load_data():
    try:
        with open("habits.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open("habits.json", "w") as f:
        json.dump(data, f, indent=4)