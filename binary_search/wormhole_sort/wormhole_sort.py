with open("input", "r") as f:
    cow_num, wormhole_num = map(int, f.readline().split())
    cows = list(map(lambda x: int(x)-1, f.readline().split())) # 0-index

    neighbors = [[] for _ in range(cow_num)]
    max_width = 0
    for _ in range(wormhole_num):
        c1, c2, width = map(int, f.readline().split())
        c1 -= 1
        c2 -= 1
        neighbors[c1].append((c2, width))
        neighbors[c2].append((c1, width))
        max_width = max(max_width, width)

lo = 0
hi = max_width + 1
valid = -1

while lo <= hi:
    mid = (lo + hi) // 2
    component = [-1] * cow_num
    curr_comp = 0

    for i in range(cow_num):
        if component[i] != -1:
            continue
        stack = [i]
        while stack:
            curr = stack.pop()
            if component[curr] != -1:
                continue
            component[curr] = curr_comp
            for neighbor, width in neighbors[curr]:
                if component[neighbor] == -1 and width >= mid:
                    stack.append(neighbor)
        curr_comp += 1

    sortable = all(component[i] == component[cows[i]] for i in range(cow_num))

    if sortable:
        valid = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(f"{-1 if valid == max_width + 1 else valid}")