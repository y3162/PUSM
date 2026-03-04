#!/bin/bash

set -e

TARGET_DIR=""
OUTPUT_DIR=""
FORCE=false

while getopts "t:o:f" opt; do
  case $opt in
    t) TARGET_DIR="$OPTARG" ;;
    o) OUTPUT_DIR="$OPTARG" ;;
    f) FORCE=true ;;
  esac
done

if [[ -z "$TARGET_DIR" ]]; then
    echo "Error: -t is required argument."
    exit 1
fi

if [[ -z "$OUTPUT_DIR" ]]; then
    echo "Error: -o is required argument."
    exit 1
fi

if [[ -d "$OUTPUT_DIR" ]]; then
    if [[ "$FORCE" = true ]]; then
        echo "Warning: $OUTPUT_DIR already exists."
        echo "Logging: Overwriting $OUTPUT_DIR"
    else
        echo "Error: $OUTPUT_DIR already exists."
        exit 1
    fi
fi

mkdir -p "$OUTPUT_DIR"
python -m src.normalize --data_dir "$TARGET_DIR" --output_dir "$OUTPUT_DIR"
