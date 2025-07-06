import sys
sys.stdin = open("input", "r")

n, m = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

total = sum(arr)
if total <= m:
    print("Yes")
else:
    print("No")
