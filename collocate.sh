#!/bin/bash
# Default to Origin (0,0,0) and Baphomet Radius (33.3) if args are missing
X=${1:-0}; Y=${2:-0}; Z=${3:-0}; R=${4:-33.3}

# Perform math using floating point compatible approach or integer fallback
cat <<JSON_EOF > inventory_intersect.json
{
  "center": {"x": $X, "y": $Y, "z": $Z},
  "bounds": {
    "cubicle": {
      "min": [$(echo "$X-$R" | bc), $(echo "$Y-$R" | bc), $(echo "$Z-$R" | bc)],
      "max": [$(echo "$X+$R" | bc), $(echo "$Y+$R" | bc), $(echo "$Z+$R" | bc)]
    },
    "sphere": {"radius": $R}
  },
  "mesh_envelope": "urn:uuid:41F052B2-5907-4389-800B-2DA9CC1D7BB3"
}
JSON_EOF
echo "[Collocation] Intersect stabilized at $X,$Y,$Z with radius $R."
