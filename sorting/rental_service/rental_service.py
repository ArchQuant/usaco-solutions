from dataclasses import dataclass
from collections import deque

@dataclass
class Store:
    q: int # offer to buy q gallons of milk
    p: int # at price p

    # descending order, price high -> low
    def __lt__(self, other: "Store"):
        return self.p > other.p
    

def rental_service():
    with open("input") as r:
        n_cows, n_stores, n_rentals = [int(i) for i in r.readline().split()]
        cows = [int(r.readline()) for _ in range(n_cows)]
        # IM - unpack "10 15" into Store(10, 15)
        stores = [Store(*map(int, r.readline().split())) for _ in range(n_stores)]
        # Wrong: cannot unpack a list [q, p] using q, p. Also, in r.readline().split will loop through q, then p.
        # stores = [Store(int(q), int(p)) for q, p in r.readline().split() for _ in range(n_stores)]
        rentals = [int(r.readline()) for _ in range(n_rentals)]

    # IM - if the most productive cow makes more in milking over rental
    # we should always milk it. 
    # Don't start from the least productive cow, because even if it makes
    # more in milking, we should still milk the most productive one, because
    # of more profit in (milking - rental) 
    cows = deque(sorted(cows, reverse= True))
    stores = deque(sorted(stores))
    rentals = deque(sorted(rentals, reverse=True))

    def value_by_milk(cow: int):
        idx = 0
        value = 0
        # IM - remember check out-of-bound idx
        while cow - stores[idx].q > 0 or idx == len(stores):
            value += stores[idx].q * stores[idx].p
            cow -= stores[idx].q
            idx += 1
        value += cow * stores[idx].p if idx < len(stores) else 0
        return value, idx, cow
    
    total = 0
    while cows:
        cow = cows[0]
        value_milk, idx, residue = value_by_milk(cow)
        value_rental = rentals[0]
        # IM - remember to check if rental is empty
        if value_milk > value_rental or not rentals:
            total += value_milk
            # update states after milking, using idx and residue
            for _ in range(idx):
                stores.popleft() 
            stores[0].q -= residue
            cows.popleft() # pop the most productive for milking
            print(f"cow: {cow}; milk: {value_milk}")
        else:
            total += value_rental
            rentals.popleft()
            cow = cows.pop() # IM - pop the least productive for rental instead
            print(f"cow: {cow}; rental: {value_rental}")
    
    print(total, file=open("output", "w"))
    '''
    input:
    cows = deque([7, 6, 4, 2, 1])
    stores = deque([Store(q=10, p=25), Store(q=15, p=15), Store(q=2, p=10)])
    rentals = deque([250, 100, 80, 40])
    
    output:
    cow: 1; rental: 250
    cow: 7; milk: 175
    cow: 6; milk: 120
    cow: 2; rental: 100
    cow: 4; rental: 80
    total = 725
    '''

if __name__ == "__main__":
    rental_service()




