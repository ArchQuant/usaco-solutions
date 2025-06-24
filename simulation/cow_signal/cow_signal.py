import sys
sys.stdin = open("input", "r")

m, n, k = map(int, input().split())
signal = [input() for _ in range(m)]

# each char twice
# each line twice
for i in range(k * m):
    for j in range(k * n):
        print(signal[i // k][j // k], end="")
    print("")