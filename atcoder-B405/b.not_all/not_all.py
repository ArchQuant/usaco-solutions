import sys
sys.stdin = open("input", "r")

n, m = [int(i) for i in input().split()]
arr = [int(a)-1 for a in input().split()]

from collections import Counter
counter = Counter(arr)
if len(counter) < m:
    print(0)
    exit()

for i in range(n-1, -1, -1):
    if counter[arr[i]] == 1:
        print(n-i)
        exit()
    counter[arr[i]] -= 1


