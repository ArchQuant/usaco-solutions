import sys
sys.stdin = open("input", "r")

n, q = [int(i) for i in input().split()]
xs = [int(i)-1 for i in input().split()]

box = [0] * n
ret = []
for x in xs:
    if x > -1:
        box[x] += 1
        ret.append(str(x+1))
    else:
        # method 1: search from the smallest count 0
        for count in range(q):
            flag = False
            for i in range(n):
                if box[i] == count:
                    box[i] += 1
                    ret.append(str(i+1))
                    flag = True
                    break
            if flag:
                break
        
print(" ".join(ret))


# method 2: scan the full n boxes, and find the smallest
ret = []
for x in xs:
    if x > -1:
        box[x] += 1
        ret.append(str(x+1))
    else:
        y = 0
        for j in range(1, n):
            if box[j] < box[y]:
                y = j
        box[y] += 1
        ret.append(str(y+1))
        
print(" ".join(ret))
