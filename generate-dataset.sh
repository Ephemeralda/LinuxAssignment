#!/bin/bash

filename=$1
num_records=$2

# Generate random numbers and ASCII strings
random_numbers=$(od -An -N$num_records -tu4 /dev/urandom | awk '{print $1}')
ascii_strings=$(openssl rand -base64 $num_records | head -c 100)

# Combine random numbers and ASCII strings
paste <(echo "$random_numbers") <(echo "$random_numbers") <(echo "$ascii_strings") > "$filename"

# Count the number of records in the file
num_lines=$(wc -l < "$filename")

echo "Generated $num_lines records in $filename"

