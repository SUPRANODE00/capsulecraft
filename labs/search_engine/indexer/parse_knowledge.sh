#!/bin/bash
LOG_SOURCE="labs/witness_forensics/logs/alignment_stream.log"
INDEX_DB="labs/search_engine/db/knowledge_index.db"

if [ -f "$LOG_SOURCE" ]; then
    # Extract timestamps and state markers using awk, clean up with sed
    awk '/TERMUX_ALIGNMENT|ALIGNMENT_TRACE/ {print "TIMESTAMP:", $1, "EVENT:", $2, "METRIC:", $4, $5, $6}' "$LOG_SOURCE" | \
    sed 's/|//g' >> "$INDEX_DB"
    echo "[INDEXER] Processed stream into shadow database."
else
    echo "[INDEXER] Stream source not found."
fi
