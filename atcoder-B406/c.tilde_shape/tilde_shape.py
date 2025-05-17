import sys
sys.stdin = open("input", "r")

N = int(input())
P = list(map(int, input().split()))

# Pad the permutation with N+1 at the start and 0 at the end
P = [N + 1] + P + [0]

q = []
# get index for peak and valley
# peak and valley must be alternatively
for i in range(N):
    if (P[i] < P[i + 1]) != (P[i + 1] < P[i + 2]):
        q.append(i)

M = len(q)
ans = 0
# variations of front and end "extras" contribute to the total counts
for k in range((M // 2) - 1):
    ans += (q[k * 2 + 1] - q[k * 2]) * (q[k * 2 + 3] - q[k * 2 + 2])

print(ans)

'''
n = int(input())
P = [int(i) for i in input().split()]

up = [False] * n
down = [False] * n
peak = [False] * n
valley = [False] * n

for i in range(1, n):
    if P[i] > P[i-1]:
        up[i] = True
    else:
        down[i] = True

for i in range(1, n-1):
    if P[i-1] < P[i] > P[i+1]:
        peak[i] = True
    elif P[i-1] > P[i] < P[i+1]:
        valley[i] = True

count = 0
for l in range(1, n-4):
    if down[l] or valley[l]:
        continue
    peak_count = 0
    valley_count = 0
    for r in range(l, n):
        peak_count += peak[r]
        valley_count += valley[r]
        if r - l >= 2 and peak_count == 1 and valley_count == 1:
            count += 1
        elif peak_count > 1 or valley_count > 1:
            break
print(count)

'''


