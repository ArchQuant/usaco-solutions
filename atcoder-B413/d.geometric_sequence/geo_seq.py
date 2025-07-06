import sys
sys.stdin = open("input", "r")

T = int(input())
for _ in range(T):
    N = int(input()) 
    raw_arr = [int(i) for i in input().split()]
    if N == 2:
        print("Yes")
        continue
    # IM: if all abs equal, sorting the abs will be random order -> failure
    if all(abs(a) == abs(raw_arr[0]) for a in raw_arr):
        s = sum(1 if a > 0 else -1 for a in raw_arr)
        if s == N or s == -N or s == 0 or s == -1 or s == 1:
            print("Yes")
        else:
            print("No")
        continue

    arr = sorted(raw_arr, key=abs)
    a0 = arr[0]
    a1 = arr[1]
    for i in range(1, N-1):
        if arr[i] * a1 != arr[i+1] * a0:
            print("No")
            break
    else:
        print("Yes")

