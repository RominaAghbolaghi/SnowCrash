#!/bin/bash

# Cipher and Encoding Analyzer

if [ -z "$1" ]; then
    echo "Usage: ./script.sh <text>"
    exit 1
fi

s="$1"

echo "Original: $s"
echo "----------------------------"

for n in $(seq 1 25); do
    alphabet="abcdefghijklmnopqrstuvwxyz"
    rotated="${alphabet:$n}${alphabet:0:$n}"

    result=$(echo "$s" | tr 'abcdefghijklmnopqrstuvwxyz' "$rotated")

    echo "Shift $n: $result"
done
