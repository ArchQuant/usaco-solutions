import sys
sys.stdin = open("input", "r")


a, b = [int(i) for i in input().split()]

l = int(a/b)
r = l+1

print(l if (a/b - l) < (r - a/b) else r)