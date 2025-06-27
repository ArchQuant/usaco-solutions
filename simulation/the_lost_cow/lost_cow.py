import sys
sys.stdin = open("input", "r")

x, y = [int(i) for i in input().split()]

trip = 1
total = 0
# use while loop, because there is a terminal condition
# each time didn't reach y, will travel twice the current trip, back to x
while trip < abs(y - x):
    trip *= 2
    total += trip
total += abs(y - x)
print(total)


