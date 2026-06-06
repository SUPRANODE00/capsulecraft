#!/bin/bash
# =========================================================================
# AXIS TELEMETRY HIVE INVENTORY CONTINUITY ENGINE
# Automated user-space background tracker for the SL1TH3R node
# =========================================================================

BROKER_IP="127.0.0.1"
BROKER_PORT="1883"
USER_NODE="SL1TH3R"
PASS_TOKEN="Hailthysel1"
TOPIC_HIVE="axis/hive/inventory"

echo "[*] Initializing SL1TH3R Hive Continuity Chain..."

while true; do
    # 1. Gather baseline asset metrics
    PKG_COUNT=$(dpkg -l | wc -l 2>/dev/null || echo "0")
    DIR_COUNT=$(find ~/.config/mosquitto -maxdepth 2 2>/dev/null | wc -l || echo "0")
    DISK_AVAIL=$(df -h ~ | awk 'NR==2 {print $4}' || echo "unknown")
    BATT_LEVEL=$(termux-battery-status 2>/dev/null | awk '/percentage/ {print $2}' | tr -d ',\n' || echo "27")
    
    # 2. Package raw metrics into a sanitized JSON string
    INVENTORY_PAYLOAD=$(cat <<JSON
{
  "node_id": "ATTACHED_NODE_SL1TH3R",
  "status": "CONTINUITY_SECURED",
  "battery": "${BATT_LEVEL}%",
  "inventory": {
    "system_packages": $PKG_COUNT,
    "hive_directories": $DIR_COUNT,
    "web_editor_node": "http://10.155.149.40:8080",
    "storage_available": "${DISK_AVAIL}"
  },
  "timestamp": $(date +%s)
}
JSON
)

    # 3. Stream payload directly to the user-space broker
    mosquitto_pub \
      -h "$BROKER_IP" \
      -p "$BROKER_PORT" \
      -u "$USER_NODE" \
      -P "$PASS_TOKEN" \
      -t "$TOPIC_HIVE" \
      -m "$INVENTORY_PAYLOAD"

    # 4. Loop interval cooldown: Sync metrics every 60 seconds
    sleep 60
done
