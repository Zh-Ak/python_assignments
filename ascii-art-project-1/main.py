"""
I checked with following code structure:
python main.py "<text>" | cat -e
"""

# input from command-line arguments (receive text from user)
import sys

if len(sys.argv) != 2: # safer structure
    exit()

text = sys.argv[1]

# open standard.txt
with open("standard.txt") as f:
    data = f.read().split("\n")

# handle \n correctly
lines = text.split("\n")

# find ASCII-art version of each character
for part in lines:
    for row in range(8):
        for char in part:
            index = ord(char) - 32
            if ord(char) < 32 or ord(char) > 126:
                continue
            start = index * 9
            print(data[start + row], end="")
        print()


