import sys
sys.stdin = open("input", "r")

# 1. use ai -> (ai, i) to record positions
# 2. For a subarray of length (l+1+r): [left], ai, [right],
# 3. We can precompute for each ai: 
#       L elements to the left are < ai
#       R elements to the right are < ai
# Then we muast have L>=l>=0, R>=r>=0.
# See the Editorial for cumulative sum trick to add/minus values

from sortedcontainers import SortedSet

def solve(n, a):
    ans = [0] * (n + 1)

    # find L and R for each (ai, i)
    asort = sorted([(a[i], i) for i in range(n)])
    integral = [[0] * (n + 3) for _ in range(3)]

    used = SortedSet([-1, n])
    # IM - add element from largest to smallest, so that all existing elements are larger
    # Firstly get R'/L' then Ri/Li,
    # R' is the absolute idx of the first value to the left that > ai
    # Ri is the relative idx (length) of the larger right-side array
    # e.g., Initially used = SortedSet([-1, 4]), curr element val = 5, idx = 2, 
    # since 5 is largest, R' is 4, because all values to the right are smaller than 5
    # Ri = R' - idx - 1 = 4 - 2 - 1 = 1, this is the length of the array to the right, 
    # i.e., all element idx [0,1,2,3], 5 is at idx2, so only idx3 element, length=1
    for val, idx in reversed(asort):
        it_Rp = used.bisect_right(idx) # idx of R_prime (R') in used (a SortedSet)
        it_Lp = it_Rp - 1

        # how many elements (on left/right) can a[idx] absorb as a maximum
        r = used[it_Rp] - idx - 1
        l = idx - used[it_Lp]  - 1

        xmin = min(l, r)
        xmax = max(l, r)

        # cumulative trick for affine functions
		# ans[0 < i <= 1+min] <- i
		# ans[1+min < i <= 1+max] <- 1+min
		# ans[1+max < i <= 1+min+max] <- 1+min - (i - (1+max))
		# ans[1+min+max < i] <- 0
        
		# ans'[0 < i <= 1+min] <- +1
		# ans'[1+min < i <= 1+max] <- 0
		# ans'[1+max < i <= 1+min+max] <- -1
		# ans'[1+min+max < i] <- 0

		# ans''[1] <- +1
		# ans''[1+min+1] <- -1
		# ans''[1+max+1] <- -1
		# ans''[1+min+max+1] <- +1
        integral[0][1] += val
        integral[0][1 + xmin + 1] -= val
        integral[0][1 + xmax + 1] -= val
        integral[0][1 + xmin + xmax + 2] += val

        used.add(idx)

    for order in range(1, 3):
        for i in range(1, n + 3):
            integral[order][i] = integral[order][i - 1] + integral[order - 1][i]

    for i in range(1, n + 1):
        ans[i] = integral[2][i]

    return ans


n = int(input())
a = list(map(int, input().split()))
anslist = solve(n, a)
for i in range(1, n + 1):
    print(anslist[i])

