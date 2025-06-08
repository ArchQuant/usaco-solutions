import sys
sys.stdin = open("input", "r")

n = int(input())
t = input()
a = input()

for ti, ai in zip(t, a):
    if ti == ai == 'o':
        print('Yes')
        exit()
print('No')