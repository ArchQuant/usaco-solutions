import sys
sys.stdin = open("input", "r")


n = int(input())
count = 0
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    if b > a:
        count += 1
print(count)