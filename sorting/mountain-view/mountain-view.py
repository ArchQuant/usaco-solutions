from dataclasses import dataclass

# use dataclass for clarity
@dataclass
class Mountain:
    x1: float
    x2: float

    # IM - If its base is fully contained by another, cannot distinguish
    # sort the bases (x1, x2) by x1, and keep record of the rightmost x2
    # compare the next base's x2 with the rightmost x2
    def __lt__(self, other: "Mountain"): # typehint uses "" for custom class
        if self.x1 == other.x1:
            # IM-large mountain first, descend not ascend, __lt__ less than uses ">"
            return self.x2 > other.x2
        return self.x1 < other.x1 # IM-sort by x1, ascend, so use "<"

def mountain_view():
    mountains = []
    with open("input") as r:
        n = int(r.readline())
        for _ in range(n): # readline n times
            x, y = [int(i) for i in r.readline().split()]
            mountains.append(Mountain(x-y, x+y))
    
    mountains.sort()

    rightmost = float("-inf")
    count = 0
    for m in mountains:
        if m.x2 > rightmost:
            rightmost = m.x2
            count += 1
    
    with open("output", "w") as f:
        f.write(str(count))

     
if __name__ == "__main__":
    mountain_view()




