#!/bin/bash
# Latitude/Longitude for Houston, TX
LAT=29.7604
LON=-95.3698
# Offset: 33.3 meters / 111,000 meters per degree
OFFSET=0.0003

LAT_MIN=$(echo "$LAT - $OFFSET" | bc -l)
LON_MIN=$(echo "$LON - $OFFSET" | bc -l)
LAT_MAX=$(echo "$LAT + $OFFSET" | bc -l)
LON_MAX=$(echo "$LON + $OFFSET" | bc -l)

echo "BBOX=$LAT_MIN,$LON_MIN,$LAT_MAX,$LON_MAX"
