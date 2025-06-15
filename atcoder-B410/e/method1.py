import sys
sys.stdin = open("input", "r")

N, H, M = [int(i) for i in input().split()]
A = []
B = []
for i in range(N):
    a, b = [int(i) for i in input().split()]
    A.append(a)
    B.append(b)

def max_monsters_defeated_optimized(N, H, M):
    dp = [[sys.maxsize] * (H + 1) for _ in range(N + 1)]

    dp[0][0] = 0

    for i in range(N):
        for j in range(H + 1):
            if dp[i][j] == sys.maxsize:
                continue

            next_health_spent = j + A[i]
            if next_health_spent <= H:
                dp[i+1][next_health_spent] = min(dp[i+1][next_health_spent], dp[i][j])

            next_magic_spent = dp[i][j] + B[i]
            if next_magic_spent <= M:
                dp[i+1][j] = min(dp[i+1][j], next_magic_spent)

    max_k = 0
    for k in range(N, -1, -1):
        for j in range(H + 1):
            if dp[k][j] != sys.maxsize:
                if dp[k][j] <= M:
                    return k

    return max_k
result = max_monsters_defeated_optimized(N, H, M,)
print(result)