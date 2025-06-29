import sys
sys.stdin = open("input", "r")

s = input()
t = set(input())

for i in range(1, len(s)):
    if s[i].isupper():
        if s[i-1] not in t:
            print("No")
            exit()
print("Yes")

