#!/bin/bash
set -e
echo "--- INITIALIZING AXIS TELEMETRY & COMPARTMENT PIPELINE ---"
python3 ~/axis_core/verify_binding.py
echo "--- PIPELINE ACTIVE & SYNCHRONIZED ---"
