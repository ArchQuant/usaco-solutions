import sys
sys.stdin = open("input", "r")

n, q = [int(i) for i in input().split()]
arr = list(range(1, n+1))
cum_rot = 0

# IM: don't do rotate, just find the index
for _ in range(q):
    qry = [int(i) for i in input().split()]
    if qry[0] == 1:
        j = (qry[1] - 1 + cum_rot)  % n
        arr[j] = qry[2]
    elif qry[0] == 2:
        j = (qry[1] - 1 + cum_rot)  % n
        print(arr[j])
    else:
        cum_rot = (cum_rot + qry[1]) % n