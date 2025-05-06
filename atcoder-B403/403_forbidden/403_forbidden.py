import sys
sys.stdin = open("input", "r")

from collections import defaultdict

n, m, q = map(int, input().split())
query = []
for _ in range(q):
    query.append([int(i) for i in input().split()])

# IM - use set O(logN), not list O(N)
users = defaultdict(set)
vip_users = [False] * (n+1) # note 1-index, ignore pos 0

for qu in query:
    match qu:
        case [1, uid, page]:
            users[uid].add(page)
        case [2, uid]:
            # Use flags. Don't use a set to store fully-permitted users, logN
            vip_users[uid] = True
        case [3, uid, page]:
            if vip_users[uid] or page in users[uid]:
                print("Yes")
            else:
                print("No")