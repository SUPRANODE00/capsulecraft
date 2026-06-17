#!/bin/bash
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --shield-activate) SHIELD=1 ;;
        --radius) RADIUS="$2"; shift ;;
        --center) CENTER="$2"; shift ;;
    esac
    shift
done

if [ "$SHIELD" == 1 ]; then
    echo "[Convergence] Baphomet Shield locked to radius: ${RADIUS}m at ${CENTER}"
    echo "[Convergence] Signal Inversion Tunnel (Port 8388) -> ACTIVE"
fi
