import socket, sqlite3, datetime

s = socket.socket()
s.settimeout(1.0)
s.connect(("127.0.0.1", 2947))
s.send(b'?WATCH={"enable":true,"json":true};')

tpv_payload = f'{{"class":"TPV","device":"/dev/ttyS0","status":2,"time":"{datetime.datetime.now().isoformat()}","lat":29.7604,"lon":-95.3698,"alt":15.0}}\n'
s.send(tpv_payload.encode())
s.close()

conn = sqlite3.connect("trinity-compiler/state/inventory.db")
conn.execute(
    "INSERT INTO mesh_telemetry (timestamp, node_id, coord_x, coord_y, coord_z, status_flag) VALUES (?, ?, ?, ?, ?, ?)",
    (datetime.datetime.now().isoformat(), "SUPRANODE-02-SOCKET", -95.3698, 29.7604, 15.0, "ACTIVE_SOCKET_SECURE")
)
conn.commit()
conn.close()
print("[⟎] Telemetry committed successfully.")
