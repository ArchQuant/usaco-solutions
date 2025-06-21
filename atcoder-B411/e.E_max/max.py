MOD = 998244353
# IM: For a problem asking for a probability or expected value in competitive programming,
# the following trick can be often applied: 
# rather than finding the probability that some maximum value coincides with a specific value,
# it is easier to find the probability that the maximum value becomes less than or equal to the specific value.
# more details in the Editorial page
import sys
sys.stdin = open("input", "r")
from bisect import bisect_left

n = int(input())
a = []
s = []

for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    s.extend(row)

s = sorted(set(s)) # all integers from any dice
k = len(s)

upd = [[] for _ in range(k)]
for idx in range(n): # n dies
    for j in range(6):
        i = bisect_left(s, a[idx][j])
        # upd[i] stores the dice index (idx, include duplicate face) that contains the value s[i]
        upd[i].append(idx)

# die1: 1 1 4 4 4 4
# die2: 1 1 1 3 3 3
print(a) #[[1, 1, 4, 4, 4, 4], [1, 1, 1, 3, 3, 3]]
print(s) # [1, 3, 4]
print(upd) # [[0, 0, 1, 1, 1], [1, 1, 1], [0, 0, 0, 0]]
# upd[0] is [0, 0, 1, 1, 1] meaning value s[0] shows on die[0] twice, and die[1] three times.
ans = 0
b = [0] * n # updating in each loop. Count how many times each die contributes
prod = 1
zero_cnt = n # number of dies that haven' contributed

# instead of loop through each die for every Sk, use cumulative product prod
for i in range(k - 1): # for each unique value except the largest one (see Editorial)
    for idx in upd[i]: # for each die with faces that has this value
        print(b) # each b[idx] will only increment
        if b[idx] == 0:
            zero_cnt -= 1 # this die starts to contribute, so zero_cnt decrement
        else:
            prod /= b[idx] # remove the old contribution
        b[idx] += 1
        prod *= b[idx] # add new contribution
    if zero_cnt == 0:
        ans -= prod * (s[i + 1] - s[i])
print(b)
ans /= 6 ** n

ans += s[k - 1] # the largetst value (see the Editorial formula)
print(ans)
