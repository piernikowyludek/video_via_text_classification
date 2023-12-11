#!/bin/bash

# Check if a file path is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

file_path=$1
base_name=$(basename -- "$file_path")
extension="${base_name##*.}"
base_name="${base_name%.*}"

# Count the total number of lines in the file
total_lines=$(wc -l < "$file_path")
# Calculate the number of lines per file, rounding up
lines_per_file=$(( (total_lines + 2) / 3 ))

# Iterate and create each split file
for i in 0 1 2; do
    start_line=$(( i * lines_per_file + 1 ))
    end_line=$(( start_line + lines_per_file - 1 ))

    # Adjust end_line for the last file
    if [ $i -eq 2 ]; then
        end_line=$total_lines
    fi

    output_file="${base_name}_${i}.$extension"

    # Extract the relevant lines using sed
    sed -n "${start_line},${end_line}p" "$file_path" > "$output_file"
    
    # Call Python script with index and output file
    srun --partition=g-queue --gres=gpu:1 python ../src/ViT_models/process_BLIP2.py  txt_file="$output_file" mode=noprompt job_index="$i"
done