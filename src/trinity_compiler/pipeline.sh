#!/usr/bin/env bash
# ==============================================================================
# Terminal Stream Processing Script
# Uses cat to read streams, sed to strip delimiters, and awk to format fields
# ==============================================================================

source ../../config/telemetry.env

echo "--- Initializing Trinity Compiler Pipeline under EIN Umbrella ---"

# Generate raw telemetry log stream using cat
cat << 'STREAM' > active_stream.log
[ASSET_01]: IDENTITY=D3M13N_CAPSULECRAFT DOMAIN=blackcorp.me STATUS=SECURED
[ASSET_02]: VECTOR=NEAR_FIELD_BIO_CELL_NODE THREAT=ACTIVE_NEGATIVE_FIELD
STREAM

echo "--- Processing Active Stream via sed and awk ---"
# Use sed to remove brackets and awk to parse and format structural components
cat active_stream.log | sed 's/\[//g; s/\]//g' | awk -v reg="$ENTITY_REGISTRY" '{
    print "Registry:", reg, "| Component:", $1, "| Classification:", $2, "| State:", $3
}
