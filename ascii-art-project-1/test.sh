#!/bin/bash

echo "Test 1: lowercase"
python main.py $"hello"

echo "Test 2: uppercase"
python main.py $"HELLO"

echo "Test 3: mixed case"
python main.py $"HeLlO"

echo "Test 4: numbers"
python main.py $"123"

echo "Test 5: spaces"
python main.py $"Hello There"

echo "Test 6: special characters"
python main.py $"{Hello & There #}"

echo "Test 7: newline"
python main.py $"Hello\nThere"

echo "Test 8: double newline"
python main.py $"Hello\n\nThere"

echo "Test 9: empty string"
python main.py $""