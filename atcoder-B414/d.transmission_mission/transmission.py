import sys
sys.stdin = open("input", "r")

# Input
N, M = map(int, input().split())
X = [int(i) for i in input().split()]

# Output
unique_X = sorted(set(X))
K = len(unique_X)

# DP: dp[i][m] = min sum of signal strengths to cover first i unique coordinates with m base stations
# dp[i][m] = min(dp[i][m], dp[j][m-1] + X[i-1] - X[j])
dp = [[float('inf')] * (M + 1) for _ in range(K + 1)]
# IM: boundary: set not only dp[i][i] to 0, but also dp[i][j>i] = 0
for i in range(K+1):
    if M+1 > i:
        for j in range(i, M+1):
            dp[i][j] = 0
    

for i in range(1, K + 1):
    for m in range(1, M + 1):
        for j in range(i):

            if dp[j][m-1] == float('inf'):
                continue
            dist = 0 if i == j + 1 else unique_X[i-1] - unique_X[j]
            strength = dist  # Signal strength = distance between endpoints
            dp[i][m] = min(dp[i][m], dp[j][m-1] + strength)

print(dp[K][M])