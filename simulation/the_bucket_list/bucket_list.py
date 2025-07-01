import sys
sys.stdin = open("input", "r")

import heapq
N = int(input())
cows = [tuple(map(int, input().split())) for _ in range(N)]
cows.sort()  # sort by start time

heap = []  # stores (end_time, buckets)
current_buckets = 0
max_buckets = 0

# Same method as LC 253. Meeting Rooms II (see below)
for start, end, b in cows:
    while heap and (prev_end :=heap[0][0]) <= start:
        _, buckets = heapq.heappop(heap)
        current_buckets -= buckets
    heapq.heappush(heap, (end, b))
    current_buckets += b
    max_buckets = max(max_buckets, current_buckets)

print(max_buckets)

"""
253. Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        used_rooms = 0
        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        end_pointer = 0
        start_pointer = 0

        while start_pointer < L:
            # a free room is available
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1

            used_rooms += 1    
            start_pointer += 1   
        return used_rooms
        
class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        free_rooms = []
        intervals.sort(key= lambda x: x[0])

        # Priority Queues: record the ending time for each meeting
        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:
            # pop the free-up room
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            # always add the new ending time
            heapq.heappush(free_rooms, i[1])
        return len(free_rooms)
        

"""