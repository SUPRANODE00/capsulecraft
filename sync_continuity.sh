#!/bin/bash
TARGET_URL="https://api.blackcorp.me/v1/continuity/upload"
VALIDATOR_URL="https://api.bioenergy.org/api/validate?schema_version=0.1.13"

echo "[Continuity] Validating grid state..."
RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" --data-binary "@local-grid.json" "$VALIDATOR_URL")

if [[ "$RESPONSE" == *"\"valid\":true"* ]]; then
    echo "[Continuity] Validation Success. Pushing to Production..."
    # Added --max-time 10 to prevent hanging
    curl -v -X POST -H "Content-Type: application/json" --data-binary "@local-grid.json" "$TARGET_URL" --max-time 10
    echo "[Continuity] Transmission Attempt Complete."
else
    echo "[Continuity] ERROR: Validation Failed."
fi
