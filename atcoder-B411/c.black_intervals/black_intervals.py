import sys
sys.stdin = open("input", "r")

n, m = [int(i) for i in input().split()]
queries = [int(i) for i in input().split()] # 1-index with padding

# IM: padding with white for simple index!!
arr = [0] * (n + 2)
count = 0
for q in queries:
    prev, next = arr[q-1], arr[q+1]
    color =  arr[q]
    color_flip = color^1 # toggle between 1 and 0
    # count only changes denpending on the block before and after
    if prev == next == color:
        count += 1
    if prev == next == color_flip:
        count -= 1
    arr[q] = color_flip
    print(count)


# a more straightforward version
arr = [0] * (n + 2)
count = 0
for q in queries:
    if arr[q] == 0: # can be further simplified by combine if and elif
        # count only changes denpending on the block before and after
        if arr[q-1] == 0 and arr[q+1] == 0:
            count += 1
        if arr[q-1] == 1 and arr[q+1] == 1:
            count -= 1
        arr[q] = 1
    elif arr[q] == 1: # IM: elif not if!!
        if arr[q-1] == 1 and arr[q+1] == 1:
            count += 1
        if arr[q-1] == 0 and arr[q+1] == 0:
            count -= 1
        arr[q] = 0
    print(count)


# alternative method
# counting pairs [i, i+1] that are different colors
# then divide by 2