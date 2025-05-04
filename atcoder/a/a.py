import sys
sys.stdin = open("input", "r")

from collections import defaultdict
count = defaultdict(int)

for c in input():
    count[c] += 1
for i in range(26):
    letter = chr(ord('a') + i)
    if count[letter] == 0:
        print(letter)
        break