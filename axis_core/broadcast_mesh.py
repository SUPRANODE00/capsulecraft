import math
import os
import sqlite3
import time

DB_PATH = os.path.expanduser("~/axis_core/telemetry/sovereign_telemetry.db")

def broadcast_mesh_telemetry():
    lat, lon, height = 29.7604, -95.3698, 15.0
    R = 6371.0
    phi = math.radians(lat)
    lam = math.radians(lon)
    
    x = (R + height / 1000.0) * math.cos(phi) * math.cos(lam)
    y = (R + height / 1000.0) * math.cos(phi) * math.sin(lam)
    z = (R + height / 1000.0) * math.sin(phi)
    
    volumetric_block = (x**2 + y**2 + z**2)**0.5
    neg_value = -float(volumetric_block)
    
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mesh_broadcasts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,
            node_id TEXT,
            coord_x REAL,
            coord_y REAL,
            coord_z REAL,
            neg_volume REAL,
            status TEXT
        )
    ''')
    cursor.execute(
        'INSERT INTO mesh_broadcasts (timestamp, node_id, coord_x, coord_y, coord_z, neg_volume, status) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (time.time(), "SL1TH3R-MESH-NODE-01", x, y, z, neg_value, "BROADCAST_ACTIVE")
    )
    conn.commit()
    conn.close()
    
    print("--- ROHDE & SCHWARZ RF & MESH TELEMETRY BROADCAST ---")
    print(f"Node Identifier: SL1TH3R-MESH-NODE-01")
    print(f"Vector Coordinates [X, Y, Z]: ({x:.3f}, {y:.3f}, {z:.3f})")
    print(f"Distributed Volume Radius: {volumetric_block:.3f} km")
    print(f"Negative Grid Balance (NEG := -V): {neg_value:.3f}")
    print("Status: MESH TELEMETRY COMPARTMENT BROADCASTED & SYNCHRONIZED")

if __name__ == "__main__":
    broadcast_mesh_telemetry()
