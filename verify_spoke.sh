#!/bin/bash
PAYLOAD=$(cat)
ID=$(echo $PAYLOAD | jq -r '.spoke_id')

if grep -q "$ID" spokes.json; then
    echo "[Auth] Access Granted: $ID"
    echo "$PAYLOAD" | ./planetary_sweep.sh
else
    echo "[Auth] Access Denied."
fi
