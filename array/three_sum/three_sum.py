n, x = map(int, input().split())
a = list(map(int, input().split()))

# store the original index for returning (1-index)
p = [(a[i], i + 1) for i in range(n)]

p.sort()

for i in range(n-2):
	left = i + 1
	right = n - 1

	while left < right:
		target = x - p[i][0]

        # two pointers for sorted array
		if p[left][0] + p[right][0] == target:
			print(p[left][1], p[right][1], p[i][1])
			exit()
		elif p[left][0] + p[right][0] < target:
			left += 1
		else:
			right -= 1

print("IMPOSSIBLE")


'''TIME EXCEEDED
O(N^2): use map[complement] cannot meet time limit
from collections import defaultdict

n, x = map(int, input().split())
arr = [int(a) for a in input().split()]

for i in range(n-2):
    first = arr[i]
    target = x - first
    seen = defaultdict(int)
    for j in range(i+1, n):
        second = arr[j]
        third = target - second
        if third in seen:
            print(f"{i+1} {seen[third]+1} {j+1}")
            exit()
        seen[second] = j
print("IMPOSSIBLE")
'''