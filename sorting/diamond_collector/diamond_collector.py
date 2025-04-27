
def diamond_collector():
    sizes = []
    with open("input") as r:
        n, k = [int(i) for i in r.readline().split()]
        sizes = [int(r.readline()) for _ in range(n)]

    sizes.sort()
    amt = [0] * n # amt so that the window length that not exceeds k

    for i in range(n):
        left = right = i
        # IM - check out-of-range; terminate at (valid + 1)
        while right < n and sizes[right] - sizes[left] <= k:
            right += 1
        amt[left] = right - left # right is not valid, so not right - left + 1

    # IM - use suffix_max, scan from beginning so don't need to worry about backwards
    suffix_max = [0] * (n+1) # padding with 0 at the end, suffix_max[n] = 0
    for i in range(n-1, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], amt[i])
    max_display = 0
    # scan all items, skip the removed item and get the nex suffix max
    for i in range(n):
        max_display = max(max_display, amt[i] + suffix_max[i+amt[i]])
    
    print(max_display, file=open("output", "w"))
    return



    # WRONG BELOW:
    # 1. cannot assume that max must be taken
    # 2. update index after removing is complex. Should think about direction: 
    # backward will be impacted by removing, but forward remains the same
    max_amt = max(amt) # max for the first case
    max_display = 0
    for j in range(n):
        if amt[j] == max_amt:
            left, right = j, j+amt[j]-1 # start+length-1, remember -1
            new_amt = amt[:left] + (amt[right+1:] if right+1<n else [])
            # update the new_amt after removing
            for i in range(left-1, -1, -1):
                # if i cannot cover left, move more left will not cover either 
                if i + new_amt[i] < left: 
                    break
                else:
                    # upper bounded by original amt or the steps moved away from left
                    # e.g. [1, 2, 1, 3, 3, 2, 1], after remove tail [3,2,1], the 3 becomes 1
                    new_amt[i] = min(left-i, new_amt[i])
            max_display = max(max_display, max_amt + max(new_amt))
    print(max_display)


# Correctness checking using official solution:
def diamond_collector_benchmark(n, k, sizes):

    sizes = sorted(sizes[:])
    amt = [0] * n # amt so that the window length that not exceeds k

    for i in range(n):
        left = right = i
        # IM - check out-of-range; terminate at (valid + 1)
        while right < n and sizes[right] - sizes[left] <= k:
            right += 1
        amt[left] = right - left # right is not valid, so not right - left + 1

    # IM - use suffix_max, scan from beginning so don't need to worry about backwards
    suffix_max = [0] * (n+1) # padding with 0 at the end, suffix_max[n] = 0
    for i in range(n-1, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], amt[i])
    max_display = 0
    for i in range(n):
        max_display = max(max_display, amt[i] + suffix_max[i+amt[i]])
    
    return max_display

# This is the official soluiton on USACO guide
def official_solusion(n, k, arr):

    arr = sorted(arr[:])
    # maximum number of diamonds assuming i is the smallest diamond
    max_diamond = [0] * (n + 1)
    j = 0
    for i in range(n):
        while j < n and arr[j] - arr[i] <= k:
            j += 1
        j -= 1
        max_diamond[i] = j - i + 1

    suffix_max = [0 for i in range(n + 1)]  # suffix maximum
    suffix_max[n - 1] = max_diamond[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(max_diamond[i], suffix_max[i + 1])

    ans = 0
    for i in range(n):
        ans = max(ans, max_diamond[i] + suffix_max[i + max_diamond[i]])
    
    return ans


if __name__ == "__main__":
    #diamond_collector()

    # correctness checking using official solution
    import random
    for _ in range(50):
        n = random.randint(2, 5000)
        k = random.randint(1, n//2)
        sizes = [random.randint(1, 5000) for _ in range(n)]
        assert official_solusion(n, k, sizes) == diamond_collector_benchmark(n, k, sizes)
    print("All passed.")

