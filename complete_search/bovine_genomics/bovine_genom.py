# IM: don't list all possible scnarios of ACGT for spotty/plain and check each {A, C}, {AG, C}, {AGT, C} ...
# because there are too many of these pairs compared to the sample size.
# Only have 100 samples, so find rules/contradict from the sample itself, i.e.,
# For each genom pos, if it is valid, it should not appear in both top/bottom

import sys
sys.stdin = open("input", "r")

n, m = [int(i) for i in input().split()]
spotted = [list(input()) for _ in range(n)]
plain = [list(input()) for _ in range(n)]

count = 0
for i in range(m): # each genom position
    duplicate = False
    for j in range(n): # each spotted
        for k in range(n): # each plain
            if spotted[j][i] == plain[k][i]:
                duplicate = True
                break
    if not duplicate:
        count += 1

print(count)


# method2: set: If a genome is present in a spotted cow but not in a plain cow, it is valid
# note: mutrual exclusive, if valid for spotted, it is also valid for plain

poss_positions = 0
for i in range(m):
	seen = set()
	for j in range(n): # each spotted
		seen.add(spotted[j][i])

	for k in range(n): # each plain
		if plain[j][i] in seen:
			break
	else:
		poss_positions += 1
print(poss_positions)