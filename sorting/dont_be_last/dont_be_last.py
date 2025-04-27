
from collections import defaultdict
NAMES = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]

def dont_be_last():
    milk_log = { name : 0 for name in NAMES}
    with open("input") as r:
        for _ in range(int(r.readline())):
            name, amt = r.readline().split()
            milk_log[name] += int(amt)

    # get the count of each amt
    counter = defaultdict(int)
    for amt in milk_log.values():
        counter[amt] += 1
    
    # cannot sort a dict, so use a list of tuples for sorting
    sorted_count = sorted([(amt, count) for amt, count in counter.items()])
    if len(sorted_count) < 2 or sorted_count[1][1] > 1:
        print("Tied")
    else:
        for name, amt in milk_log.items():
            if amt == sorted_count[1][0]:
                print(name)
    
    


if __name__ == "__main__":
    dont_be_last()
