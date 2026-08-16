import json

with open("system_manifest.json", "r") as f:
    m = json.load(f)

print(f"[INFERNAL-LOCK] System: {m['system']}")
print(f"[INFERNAL-LOCK] Grid State: {m['grid_state']}")
print(f"[INFERNAL-LOCK] Compliance: {m['compliance']}")
print(f"[INFERNAL-LOCK] Signal Integrity: {m['signal_integrity']}")
