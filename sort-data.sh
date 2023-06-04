#!/bin/bash

filename=$1

time sort -n -k1 -o "$filename.sorted" "$filename"

echo "Sorted data saved to $filename.sorted"

