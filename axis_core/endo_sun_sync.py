import math
import os
import sqlite3
import time

DB_PATH = os.path.expanduser("~/axis_core/telemetry/sovereign_telemetry.db")

def execute_endo_sun_telemetry(lat=29.7604, lon=-95.3698, height=15.0):
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
        CREATE TABLE IF NOT EXISTS endo_sun_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL,
            coord_x REAL,
            coord_y REAL,
            coord_z REAL,
            neg_volume REAL,
            status TEXT
        )
    ''')
    cursor.execute(
        'INSERT INTO endo_sun_logs (timestamp, coord_x, coord_y, coord_z, neg_volume, status) VALUES (?, ?, ?, ?, ?, ?)',
        (time.time(), x, y, z, neg_value, "ENDO_SUN_PINNED")
    )
    conn.commit()
    conn.close()
    
    print("--- AXIS ENDO-SUN VECTOR COMPILATION ---")
    print(f"GPS Input [Lat, Lon, Alt]: ({lat}, {lon}, {height}m)")
    print(f"Computed 3D Vector [X, Y, Z]: ({x:.3f}, {y:.3f}, {z:.3f})")
    print(f"Virtual Layer Shadowing Radius: {volumetric_block:.3f} km")
    print(f"Negative Grid Balance (NEG := -V): {neg_value:.3f}")
    print("Status: SHADOWING WITNESS MODEL PINNED OVER VOID — ENDO-SUN PATHWAY ACTIVE")

if __name__ == "__main__":
    execute_endo_sun_telemetry()
