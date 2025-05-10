import sys
#sys.stdin = open("input", "r")

#r, x = [int(i) for i in input().split()]

r = 1500
x = 2
range = {1 : (1600, 2999), 2: (1200, 2399)}

lo, hi = range[x]

if r >= lo and r <= hi:
    print("Yes")
else:
    print("No")

