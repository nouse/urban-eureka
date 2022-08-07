>>> from ch11 import find_cheapest_price

>>> find_cheapest_price(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0)
500
>>> find_cheapest_price(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1)
200
>>> find_cheapest_price(n=4, flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], src=0, dst=3, k=1)
6
