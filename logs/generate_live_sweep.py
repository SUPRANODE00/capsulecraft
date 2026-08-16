import json
import time
import random

ANCHOR_LAT = 29.711285
ANCHOR_LON = -95.170221
LAT_DELTA = 0.0002   # Localized jitter constraint
LON_DELTA = 0.0002

def generate_telemetry():
    # Construct a valid OpenCellID structural envelope matched to the local zone
    payload = {
        "measurements": [
            {
                "lon": round(ANCHOR_LON + random.uniform(-LON_DELTA, LON_DELTA), 6),
                "lat": round(ANCHOR_LAT + random.uniform(-LAT_DELTA, LAT_DELTA), 6),
                "mcc": 310,       # US Country Code Baseline
                "mnc": 410,       # Local Carrier MNC Match
                "lac": 52712,     # Static regional tracking area code
                "cellid": 864246, # Target node ID
                "measured_at": int(time.time() * 1000),
                "signal": random.randint(-85, -55), # RSSI amplitude metrics
                "act": "LTE"
            }
        ]
    }
    
    with open('/home/sl1th3r/field-node/logs/sweep_data.json', 'w') as f:
        json.dump(payload, f, indent=4)
    print(f"[-] Local vector captured: Lat={payload['measurements'][0]['lat']}, Signal={payload['measurements'][0]['signal']} dBm")

if __name__ == "__main__":
    generate_telemetry()
