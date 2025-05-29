import sys
sys.stdin = open("input", "r")

n = int(input())
s = str(input())

# length n will always be an answer, we need to find shorter ones
# so scan from length 1 upwards
# use set to track duplicate
for k in range(1, n+1):
    patterns = set()
    valid = True
    for i in range(n-k+1):
        if s[i:i+k] in patterns:
            valid = False
            break
        patterns.add(s[i:i+k])
    if valid:
        print(k)
        exit()
