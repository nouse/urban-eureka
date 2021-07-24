from typing import List
from heapq import heappush, heappop


def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # start snippet init
    d = [[] for _ in range(n)]
    for flight in flights:
        d[flight[0]].append((flight[1], flight[2]))
    choices = []
    for dest, price in d[src]:
        heappush(choices, (price, k, dest))
    # end snippet init
    # start snippet loop
    while choices:
        price, stop, dest = heappop(choices)
        if dest == dst:
            return price

        if stop > 0:
            for ndest, nprice in d[dest]:
                heappush(choices, (price+nprice, stop-1, ndest))
    return -1
    # end snippet loop
