import sys
sys.stdin = open("input", "r")

n = int(input())
arr = [int(i) for i in input().split()]
k = int(input())

count = 0
for a in arr:
    if k <= a:
        count += 1
print(count)