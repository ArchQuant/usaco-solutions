import sys
sys.stdin = open("input", "r")

n = int(input())
count = 0
ret = ""
for _ in range(n):
    c, l = input().split()
    count += int(l)
    if count > 100:
        print("Too Long")
        exit()
    ret += c * int(l)
print(ret)