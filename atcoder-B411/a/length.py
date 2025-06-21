import sys
sys.stdin = open("input", "r")

p = input()
l = int(input())

print("Yes" if len(p) >= l else "No")