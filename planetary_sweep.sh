#!/bin/bash
# Process input as a single stream
PAYLOAD=$(cat)

# Extract coordinates
X=$(echo $PAYLOAD | jq -r '.vector.x')
Y=$(echo $PAYLOAD | jq -r '.vector.y')
Z=$(echo $PAYLOAD | jq -r '.vector.z')

# Calculate distance using awk for reliable floating-point math
DIST=$(awk -v x="$X" -v y="$Y" -v z="$Z" 'BEGIN {print sqrt(x*x + y*y + z*z)}')

echo "[Sweep] Vector: ($X, $Y, $Z) | Flux: $DIST nm" >> planetary_signal.log
