# IM - the direction is the key. When forward doesn't work out, try backward.
# e.g. if dp[i][j] marking the start doesn't work, try it marking the end.
# DP grid with text1 on the y axis, text2 on the x axis.
# dp[i][j] is not the longest for t1[:i+1] and t2[:j+1], but for t1[i:] and t2[j"]
# This design also determines the boundary and padding.
def longestCommonSubsequence(text1: str, text2: str) -> int:
    # pad with 0 on grid bottom and right side
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    
    # since there is an extra padding, dp[N] are zeros, thus start from dp[N-1]
    for col in reversed(range(len(text2))): # N-1, N-2, ... 0
        for row in reversed(range(len(text1))):
            if text2[col] == text1[row]:
                # diagonal move
                dp[row][col] = 1 + dp[row + 1][col + 1]
            else:
                dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
    
    return dp[0][0]