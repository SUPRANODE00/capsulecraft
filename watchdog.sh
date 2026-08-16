#!/bin/bash
REPO_DIR="$HOME/Tripartite-Compiler-Telemetry-Repository-Architecture/Tripartite-Compiler-Telemetry-Repository-Architecture/Tripartite-Compiler-Telemetry-Repository-Architecture"
cd "$REPO_DIR"

while true; do
    echo "[*] Starting broadcast_mesh.py listener..."
    python3 src/broadcast_mesh.py
    echo "[!] Listener crashed, restarting in 5 seconds..."
    sleep 5
done
