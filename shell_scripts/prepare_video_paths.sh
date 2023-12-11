#!/bin/bash

# Check if a directory path is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory_path> <output_file>"
    exit 1
fi

directory_path=$1
output_file=$2

# List all files in the directory and its subdirectories
find "$directory_path" -type f > "$output_file"

echo "File paths saved to $output_file"