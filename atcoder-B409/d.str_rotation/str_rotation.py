import sys
sys.stdin = open("input", "r")

# IM: more efficient: the char can be compared with each other directly, no need to convert to int
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n == 1:
        print(s)
        continue
    to_move = 0
    # char to be moved: only check up until the first "less than"
    for i in range(0, n-1):
        if s[i] > s[i+1]:
            to_move = i
            break
    else: # monotonically increase, so answer remain unchanged
        print(s)
        continue # IM: remember to add "continue"!!
    move_to = -1
    # move-to location: only check up until the first larger element
    for i in range(to_move+1, n):
        if s[i] > s[to_move]:
            move_to = i
            break
    else:
        move_to = n # monotonically increase, so 
    print(s[:to_move] + s[to_move+1:move_to] + s[to_move] + s[move_to:])

# less efficient: convert str to int list
t = int(input())
for _ in range(t):
    n = int(input())
    s = [ord(c) - ord('a') for c in list(input())]
    if n == 1:
        print(chr(s[0] + ord('a')))
        continue
    to_move = 0
    # char to be moved: only check up until the first "less than"
    for i in range(0, n-1):
        if s[i] > s[i+1]:
            to_move = i
            break
    else: # monotonically increase, so answer remain unchanged
        print("".join(chr(si + ord('a')) for si in s))
        continue # IM: remember to add "continue"!!
    move_to = -1
    # move-to location: only check up until the first larger element
    for i in range(to_move+1, n):
        if s[i] > s[to_move]:
            move_to = i
            break
    else:
        move_to = n # monotonically increase, so 
    s.insert(move_to, s[to_move])
    s.pop(to_move)
    print("".join(chr(si + ord('a')) for si in s))
