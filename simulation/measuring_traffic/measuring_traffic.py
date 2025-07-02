import sys
sys.stdin = open("input", "r")
num_miles = int(input())

segment_type = []
start = []
end = []

for m in range(num_miles):
    curr_type, s, e = input().split()
    segment_type.append(curr_type)
    start.append(int(s))
    end.append(int(e))

low = 0
high = float("inf")

# IM: scan backward since looking for prior status
for m in range(num_miles - 1, -1, -1):
	if segment_type[m] == "none":
		low = max(low, start[m])
		high = min(high, end[m])
	elif segment_type[m] == "off":
		low += start[m] # adding back the off ones. smaller first
		high += end[m]
	elif segment_type[m] == "on":
		low -= end[m] # larger ones first
		high -= start[m]
		# IM: zero if low becomes negative
		low = max(0, low)

print(low, high)

low = 0
high = float("inf")

# IM: scan forward to get post status
for m in range(num_miles):
	if segment_type[m] == "none":
		low = max(low, start[m])
		high = min(high, end[m])
	elif segment_type[m] == "on":
		low += start[m] # adding the on ones
		high += end[m]
	elif segment_type[m] == "off":
		low -= end[m] # minus the off ones, larger first
		high -= start[m]
		low = max(0, low)

print(low, high)