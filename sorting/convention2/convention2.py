from dataclasses import dataclass
import heapq
from collections import deque

@dataclass
class Cow:
    s: int # seniority, 0 is the highest
    a: int # arriving time
    t: int # time spent eating grass

    def __lt__(self, other: "Cow"):
        return self.s < other.s
    

def convention2():
    cows = []
    with open("input") as r:
        n = int(r.readline())
        for i in range(n):
            a, t = [int(i) for i in r.readline().split()]
            cows.append(Cow(i, a, t))
    
    # IM - First sort by arriving time, second sort by seniority
    #   this will handle the corner case of same arriving time.
    cows.sort(key=lambda x: (x.a, x.s))
    next_available = 0
    q = [] # waiting line (heapq)
    max_wait = 0
    cows = deque(cows) # arrival sequence (deque)

    # IM - Find the states, the transition, and termination
    # State 1: empty q, cows[0].a > next_available (include initial state)
    #          Update the next_available, -> State 2
    # Note: all q items have a < next_available
    # State 2: non-empty q, empty cows or cows[0].a > next_available (cannot intake new cows)
    #          heappop(q), update next_available and max_wait, -> State 2,1,3,4
    # State 3: any q, cows[0] < next_available (must add new cows to q)
    # Note: this could happen when next_available increases during State 2, must add to q
    #          heappush(q, cows[0]) -> State 2 or 3
    # State 4: empty q, empty cows (Termination)

    # IM - since there is a termination (State 4),
    # use while loop, and if/elif to handle each State
    # not "for cow in cows"

    while q or cows:
        if not q and cows[0].a > next_available:
            next_available = cows[0].a + cows[0].t
            cows.popleft() # don't forget to popleft
        elif q and (not cows or cows[0].a > next_available):
            max_wait = max(max_wait, next_available - q[0].a)
            next_available += q[0].t
            heapq.heappop(q)
        # IM - corner case: use "<=" not "<"
        elif cows and cows[0].a <= next_available: 
            heapq.heappush(q, cows.popleft())
        else:
            print("Should not reach")
            break

    print(max_wait, file=open("output", "w"))

if __name__ == "__main__":
    convention2()






# This is the official solution which was used as a benchmark for correctness checking
def convention2_official_solution(cows_in):
    cows = []
    with open("convention2.in") as read:
        for c in range(int(read.readline())):
            start, duration = [int(i) for i in read.readline().split()]
            cows.append((c, start, duration))

    # sort by arrival time
    cows.sort(key=lambda c: c[1])

    time = 0
    curr = 0
    longest_wait = 0

    # sorted by priority so that the highest seniority starts eating first
    waiting = []
    # as long as we haven't processed all cows or there are still cows waiting
    while curr < len(cows) or waiting:
        # this cow can be processed
        if curr < len(cows) and cows[curr][1] <= time:
            heapq.heappush(waiting, cows[curr])
            curr += 1
        # no cow waiting, skip to the next cow
        elif not waiting:
            # set time to the ending time of the next cow
            time = cows[curr][1] + cows[curr][2]
            curr += 1
        else:
            # process the next cow
            next_cow = heapq.heappop(waiting)
            longest_wait = max(longest_wait, time - next_cow[1])

            # set the time to when this cow finishes
            time += next_cow[2]

    print(longest_wait, file=open("convention2.out", "w"))

