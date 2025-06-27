import sys
sys.stdin = open("input", "r")

m, n, k = map(int, input().split())
signal = [input() for _ in range(m)]

# method1: top-down indexing
# each char twice
# each line twice
for i in range(m):
    new_line = ""
    for j in range(n):
        for _ in range(k):
            new_line += (signal[i][j])
    for _ in range(k):
        print(new_line)

# method2: bottom-up indexing
print("Method 2:")
for i in range(k * m):
    for j in range(k * n):
        print(signal[i // k][j // k], end="")
    print("")

