import os
import sqlite3
import numpy as np
from datetime import datetime

print("--- INITIALIZING TRINITY PRISM MESH TELEMETRY ENGINE ---")

# Ensure state directory exists before connecting
os.makedirs("trinity-compiler/state", exist_ok=True)
db_path = "trinity-compiler/state/inventory.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create telemetry coordinate table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mesh_telemetry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        node_id TEXT,
        coord_x REAL,
        coord_y REAL,
        coord_z REAL,
        status_flag TEXT
    )
''')

# Define coordinate vectors mapping Left (Vegedulah) & Right (Bogedurah) Axes
node_telemetry = [
    ("SUPRANODE-00-LEFT", -200.0, 800.0, -100.0, "ACTIVE_SECURE"),
    ("SUPRANODE-00-RIGHT", 200.0, 800.0, -100.0, "ACTIVE_SECURE")
]

timestamp = datetime.utcnow().isoformat()
for node_id, x, y, z, flag in node_telemetry:
    cursor.execute('''
        INSERT INTO mesh_telemetry (timestamp, node_id, coord_x, coord_y, coord_z, status_flag)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, node_id, x, y, z, flag))

conn.commit()
conn.close()

print(f"[+] Spatial telemetry matrix successfully committed to {db_path}")
print("[+] Mesh coordinate mapping and state inventory fully synchronized.")
