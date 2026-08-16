#!/bin/bash
# Registration Utility for Genesis Convergence
ID=$2
TYPE=$4
AUTH=$6

echo "{\"id\": \"$ID\", \"type\": \"$TYPE\", \"auth\": \"$AUTH\", \"status\": \"REGISTERED\"}" >> spokes.json
echo "[Registry] Spoke $ID ($TYPE) registered at the pillar root."
