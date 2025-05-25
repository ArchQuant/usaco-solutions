import sys
sys.stdin = open("input", "r")

# IM - max(cum_max_forward + cum_max_backward + curr)
def running_miles(n, a):

    pref = [0] * n
    suff = [0] * n

    # goal: max(b1 + b2 + b3 - (r-l))
    for i in range(n):
        # to account for -(r-l), we embed the -r and +l into each beauty level
        # so taht we only need to find max(b1' + b2' + b3')
        pref[i] = a[i] + i # +l
        suff[i] = a[i] - i # -r

    # find cumulative max
    for i in range(1, n):
        pref[i] = max(pref[i], pref[i - 1])
    for i in range(n - 2, -1, -1):
        suff[i] = max(suff[i], suff[i + 1])

    ans = 0
    for i in range(1, n - 1):
        ans = max(ans, pref[i - 1] + suff[i + 1] + a[i])
    print(ans)
   
num_trails = int(input())
for _ in range(num_trails):
    n = int(input())
    a = list(map(int, input().split()))
    running_miles(n, a)