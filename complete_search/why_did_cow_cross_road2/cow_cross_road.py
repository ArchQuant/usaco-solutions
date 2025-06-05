import sys
sys.stdin = open("input", "r")

cross = list(input())

# IM: turn A-Z to 0-25 and store with list (dict is less efficient due to hash)
first = [-1 for _ in range(26)]
second = [-1 for _ in range(26)]

for v, c in enumerate(cross):
	c_id = ord(c) - ord("A")
	if first[c_id] == -1:
		first[c_id] = v
	else:
		second[c_id] = v

crossing_pairs = 0
# brutal force all pairs (i, j)
for i in range(26):
	for j in range(26):
        # here i < j is not guarranteed, only use one direction
		# i.e., only valid for i < j and ignore the cases j > i
		crossing_pairs += first[i] < first[j] and \
			first[j] < second[i] and second[i] < second[j]

print(crossing_pairs)