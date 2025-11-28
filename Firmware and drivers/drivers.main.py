import json
import os
import threading
import tkinter as tk
from tkinter import filedialog
import keyboard
import winsound

CONFIG_FILE = "config.json"

default_config = {
    "modes": [
        {"name": "Mode 0", "buttons": {
            "f13": {"type": "play_sound", "value": "sounds/mode0_btn0.wav"},
            "f14": {"type": "play_sound", "value": "sounds/mode0_btn1.wav"},
            "f15": {"type": "play_sound", "value": "sounds/mode0_btn2.wav"},
            "f16": {"type": "play_sound", "value": "sounds/mode0_btn3.wav"},
            "f17": {"type": "play_sound", "value": "sounds/mode0_btn4.wav"}
        }},
        {"name": "Mode 1", "buttons": {
            "f13": {"type": "play_sound", "value": "sounds/mode1_btn0.wav"},
            "f14": {"type": "play_sound", "value": "sounds/mode1_btn1.wav"},
            "f15": {"type": "play_sound", "value": "sounds/mode1_btn2.wav"},
            "f16": {"type": "play_sound", "value": "sounds/mode1_btn3.wav"},
            "f17": {"type": "play_sound", "value": "sounds/mode1_btn4.wav"}
        }},
        {"name": "Mode 2", "buttons": {
            "f13": {"type": "play_sound", "value": "sounds/mode2_btn0.wav"},
            "f14": {"type": "play_sound", "value": "sounds/mode2_btn1.wav"},
            "f15": {"type": "play_sound", "value": "sounds/mode2_btn2.wav"},
            "f16": {"type": "play_sound", "value": "sounds/mode2_btn3.wav"},
            "f17": {"type": "play_sound", "value": "sounds/mode2_btn4.wav"}
        }},
    ],
    "last_mode": 0
}

if not os.path.exists(CONFIG_FILE):
    os.makedirs("sounds", exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(default_config, f, indent=2)

with open(CONFIG_FILE, "r") as f:
    config = json.load(f)

current_mode = config.get("last_mode", 0)

def save_config():
    config["last_mode"] = current_mode
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def do_action(mode_idx, fkey):
    btn = config["modes"][mode_idx]["buttons"].get(fkey)
    if not btn:
        return
    if btn["type"] == "play_sound":
        path = btn["value"]
        if os.path.exists(path):
            winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)

F_KEYS = ["f13", "f14", "f15", "f16", "f17"]

def make_handler(fkey):
    def handler():
        threading.Thread(target=do_action, args=(current_mode, fkey), daemon=True).start()
    return handler

for fk in F_KEYS:
    keyboard.add_hotkey(fk, make_handler(fk))

def cycle_mode():
    global current_mode
    current_mode = (current_mode + 1) % len(config["modes"])
    save_config()
    update_mode_label()

keyboard.add_hotkey("ctrl+alt+m", cycle_mode)

root = tk.Tk()
root.title("KMK Drivers Soundboard")

mode_label = tk.Label(root, text="", font=("Segoe UI", 16))
mode_label.pack(pady=8)

def update_mode_label():
    mode_label.config(text=f"Mode {current_mode}: {config['modes'][current_mode]['name']}")

update_mode_label()

root.mainloop()
