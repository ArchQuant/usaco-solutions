import sys
sys.stdin = open("input", "r")

n = int(input())
arr = [int(i) for i in input().split()]

# IM: recursion - for each apple, put in 1st or 2nd group
# the termination is the diff when exhauste all apples
# for all i < n, it will recursively add 1
# eventually, between the two termination value, pick the smaller one

def recursive_add(i, sum1, sum2):
    if i == n:
        return abs(sum1 - sum2)

    return min(
        recursive_add(i+1, sum1 + arr[i], sum2),
        recursive_add(i+1, sum1, sum2 + arr[i])
    )

print(recursive_add(0, 0, 0))

# Method2: bitmask
# exhaust all masks range(1 << n), i.e., between 0 and 2^n - 1 (in total 2^n scenarios)
ans = float('inf')
for mask in range(1 << n):
    # for each mask scenario, find the diff and keep min
    sum1 = sum2 = 0
    for i in range(n):
        if mask & (1 << i):
            sum1 += arr[i]
        else:
            sum2 += arr[i]
    ans = min(ans, abs(sum1 - sum2))

print(ans)