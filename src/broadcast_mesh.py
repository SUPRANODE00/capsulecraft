import os, sqlite3, time, subprocess, stat

DB_NAME = "config/telemetry.db"
FIFO_PATH = "config/telemetry.fifo"

def init_db():
    os.makedirs("config", exist_ok=True)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coordinates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            hex_stream TEXT,
            x_coord REAL,
            y_coord REAL,
            z_coord REAL
        )
    """)
    conn.commit()
    conn.close()

def parse_hex_to_coordinates(hex_stream):
    val = int(hex_stream[:6], 16) if len(hex_stream) >= 6 else 123456
    x = (val & 0xFF) * 0.1
    y = ((val >> 8) & 0xFF) * 0.1
    z = ((val >> 16) & 0xFF) * 0.1
    return x, y, z

def run_listener():
    init_db()
    if os.path.exists(FIFO_PATH):
        try:
            mode = os.stat(FIFO_PATH).st_mode
            if not stat.S_ISFIFO(mode):
                os.remove(FIFO_PATH)
                os.mkfifo(FIFO_PATH)
        except Exception:
            os.remove(FIFO_PATH)
            os.mkfifo(FIFO_PATH)
    else:
        os.mkfifo(FIFO_PATH)

    print(f"[*] Listening on FIFO: {FIFO_PATH}")
    while True:
        with open(FIFO_PATH, "r") as fifo:
            for line in fifo:
                hex_stream = line.strip()
                if not hex_stream:
                    continue
                x, y, z = parse_hex_to_coordinates(hex_stream)
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO coordinates (timestamp, hex_stream, x_coord, y_coord, z_coord) VALUES (?, ?, ?, ?, ?)", (time.strftime("%Y-%m-%d %H:%M:%S"), hex_stream, x, y, z))
                conn.commit()
                conn.close()
                print(f"[+] Processed Hex -> Coordinates: X={x:.2f}, Y={y:.2f}, Z={z:.2f}")
                subprocess.run(["git", "add", "."], check=False)
                subprocess.run(["git", "commit", "-m", f"Auto-sync telemetry pipeline heartbeat: {time.strftime("%Y-%m-%d %H:%M:%S")}"], check=False)
                subprocess.run(["git", "push", "origin", "main"], check=False)

if __name__ == "__main__":
    run_listener()
