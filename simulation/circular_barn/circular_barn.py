import sys
sys.stdin = open("input", "r")

room_num = int(input())
rooms = [int(input()) for _ in range(room_num)]

total_cows = sum(rooms)

min_dist = float("inf")
# try each door and get min
for unlock in range(room_num):
	dist = 0
	cows_left = total_cows # IM: all cows will need to pass the first door
	for r in range(room_num):
		cows_left -= rooms[(unlock + r) % room_num] # decrement after each room
		dist += cows_left
	min_dist = min(min_dist, dist)

print(min_dist)