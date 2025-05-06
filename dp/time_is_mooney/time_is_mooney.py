
from collections import defaultdict
with open("input") as r:
    N, M, C = map(int, r.readline().split())
    m = [int(i) for i in r.readline().split()]
    adj = defaultdict(list)
    for _ in range(M):
        a, b = map(int, r.readline().split())
        adj[a-1].append(b-1) # there exits a road from a -> adj[a]
    

# dp[t][curr]: Most mooney on t day, at curr city
# for next in adj[curr]:
#   dp[t+1][next] = max(dp[t+1][next], dp[t][curr] + mooney[next]) - C*((t+1)^2 - t^2)
# 
# IM - boundary: starting from 1, no need to worry about end, just use max time
# direction: from 1 to the next, will automatically handle the case if back to 1

TIME = 10
dp = [[float('-inf')] * len(adj) for _ in range(TIME)]
dp[0][0] = 0

# use the max time as termination
for t in range(TIME-1):
    # IM - should not use BFS here, because we have both directions.
    # Just use the brutal force to loop through each city at each time point
    for curr in range(N): 
        if dp[t][curr] == float('-inf'):
            continue
        for next in adj[curr]:
            dp[t+1][next] = max(dp[t+1][next], dp[t][curr] + m[next]) - C * ((t+1)**2 - t**2)

res = max(row[0] for row in dp)
print(res)



        
