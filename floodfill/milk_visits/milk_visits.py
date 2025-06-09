with open("input") as read:
	farm_num, query_num = [int(i) for i in read.readline().split()]
	farms = read.readline()
	neighbors = [[] for _ in range(farm_num)]
	for f in range(farm_num - 1):
		f1, f2 = [int(i) - 1 for i in read.readline().split()]
		neighbors[f1].append(f2)
		neighbors[f2].append(f1)

	queries = []
	for _ in range(query_num):
		query = read.readline().split()
		query[0], query[1] = int(query[0]) - 1, int(query[1]) - 1
		queries.append(query)

component_num = 0
component = [-1 for _ in range(farm_num)]
for f in range(farm_num):
	if component[f] != -1:
		continue
	frontier = [f]
	curr_type = farms[f]
	while frontier:
		curr = frontier.pop()
		component[curr] = component_num
		for n in neighbors[curr]:
			if farms[n] == curr_type and component[n] == -1:
				frontier.append(n)
	component_num += 1

with open("milkvisits.out", "w") as written:
	for a, b, milk in queries:
		if component[a] == component[b]:
			"""
			If a & b are in the same component,
			check if the milk type is the same as the one the farmer likes
			"""
			print(1 if farms[a] == milk else 0, end="", file=written)
		else:
			# Output 1 otherwise because both milk types will be visited
			print(1, end="", file=written)
	print(file=written)