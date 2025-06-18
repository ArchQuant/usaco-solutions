import sys
sys.stdin = open("input", "r")

n = int(input())
shell_pos = list(range(3)) # IM: use this to track three scenarios at once
counter = [0] * n
for _ in range(n):
    a, b, g = [int(i) - 1 for i in input().split()]
    shell_pos[a], shell_pos[b] = shell_pos[b], shell_pos[a]
    # IM: if originally at pos=1, only counter[g==1] will increment
    # similarly for original pos = 2 or 3
    # there for it tracks all three scenarios at once.
    counter[shell_pos[g]] += 1

print(max(counter))
