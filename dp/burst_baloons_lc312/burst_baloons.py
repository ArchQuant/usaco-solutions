nums = [3,1,5,8]

# Padding: add 1's to both ends of nums
# dp[i][j]: is max betwen inner dp[i+1][j-1]
# i.e. we only burst ballons [i+1, j-1]
nums = [1] + nums + [1]
n = len(nums)
dp = [[0] * n for _ in range(n)]

# For each possible length of subarray
for gap in range(2, n):
    for left in range(n - gap):
        right = left + gap
        
        res = 0
        # IM: Try each balloon as the last one to burst
        for last in range(left+1, right):
            coins = nums[left] * nums[last] * nums[right]
            res = max(res, coins + dp[left][last] + dp[last][right])
        dp[left][right] = res
        
print(dp[0][n-1])

# method2: same dp but with recursion
from functools import cache
nums = [3,1,5,8]
nums = [1] + nums + [1]

@cache
def dp(i, j):
    if j-i == 1:
        return 0
    res = float('-inf')
    for k in range(i+1, j):
        res = max(res, dp(i,k) + nums[i]*nums[k]*nums[j] + dp(k,j))
    return res

print(dp(0,len(nums)-1))