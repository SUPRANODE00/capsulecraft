import os

DISCLAIMER_FILE = "README.md"
TOGGLE_FLAG = "config/statecraft_toggle.flag"

def enable_disclaimer():
    os.makedirs("config", exist_ok=True)
    with open(TOGGLE_FLAG, "w") as f:
        f.write("ENABLED")
    print("[+] State-craft disclaimer ENABLED.")

def disable_disclaimer():
    if os.path.exists(TOGGLE_FLAG):
        os.remove(TOGGLE_FLAG)
    print("[+] State-craft disclaimer DISABLED.")

def is_enabled():
    return os.path.exists(TOGGLE_FLAG)
