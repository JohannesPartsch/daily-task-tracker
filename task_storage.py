import json
import os
from datetime import date

TASKS_FILE = "tasks.json"

def load_tasks():
    # Datei fehlt? Leere Struktur zurückgeben
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    # 🔁 Automatische Migration: Liste → neues Format
    if isinstance(data, list):
        data = {
            "last_opened": str(date.today()),
            "tasks": data
        }
        save_data(data)
        print("🔧 Alte Struktur erkannt – automatisch migriert.")

    # Tägliches Zurücksetzen
    today_str = str(date.today())
    if data.get("last_opened") != today_str:
        for task in data.get("tasks", []):
            task["done"] = False
        data["last_opened"] = today_str
        save_data(data)
        print("🔄 Neuer Tag erkannt – Aufgaben wurden zurückgesetzt.")

    return data.get("tasks", [])

def save_tasks(tasks):
    data = {
        "last_opened": str(date.today()),
        "tasks": tasks
    }
    save_data(data)

def save_data(data):
    with open(TASKS_FILE, "w") as f:
        json.dump(data, f, indent=2)
