#!/bin/bash
read SPOKE_ID
if grep -q "$SPOKE_ID" spokes.json; then
    echo "[Auth] Access Granted: $SPOKE_ID"
    ./axis_converge.sh --shield-activate
else
    echo "[Auth] Access Denied."
fi
