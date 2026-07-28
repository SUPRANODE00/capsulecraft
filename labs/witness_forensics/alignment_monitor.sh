#!/bin/bash
LOG_DIR="labs/witness_forensics/logs"
LOG_FILE="$LOG_DIR/alignment_stream.log"
mkdir -p "$LOG_DIR"

while true; do
    TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    # Extract active connectivity and routing metrics
    ROUTE_STATE=$(ip route show | awk '/default/ {print "Gateway:", $3, "Dev:", $5}')
    CONNECTION_METRICS=$(ss -t -a | awk 'BEGIN {count=0} {count++} END {print "Active Sockets:", count}')

    LOG_ENTRY="[$TIMESTAMP] ALIGNMENT_TRACE | $ROUTE_STATE | $CONNECTION_METRICS"
    echo "$LOG_ENTRY" >> "$LOG_FILE"

    # Maintain rolling window or sleep interval for continuous loop
    sleep 60
done
