import sys
sys.stdin = open("input", "r")

n = int(input())
# IM: use this to track three scenarios at once
# explain: shell_pos = [empty, pebble, empty] as [0, 1, 0]
# after shuffle, shell_pos[guess] = 1 if hit, 0 if miss
# Now mark the shell_pos as [0, 1, 2], and counter [0, 0, 0]
# each shell_pos[g] tracks one of the original pos of the pebble
# counter[orignal pos] count for each pebble scenario
shell_pos = list(range(3))
counter = [0] * n
for _ in range(n):
    a, b, g = [int(i) - 1 for i in input().split()]
    shell_pos[a], shell_pos[b] = shell_pos[b], shell_pos[a]
    # IM: only counter[g==current pebble] will increment
    # shell_pos[g] tracks the original pos of the pebble
    # therefore it tracks all three scenarios at once.
    counter[shell_pos[g]] += 1

print(max(counter))
