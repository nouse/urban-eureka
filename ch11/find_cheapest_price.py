from typing import List


def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # start snippet init
    d = [[] for _ in range(n)]
    for flight in flights:
        d[flight[0]].append((flight[1], flight[2]))
    r = float("inf")
    # end snippet init
    # start snippet dst
    choices = [(dest, price, k) for dest, price in d[src]]
    while choices:
        dest, price, stop = choices.pop()
        # 如果找到了到达目的城市的路径，更新返回值
        if dest == dst:
            r = min(r, price)

        if stop > 0 and price < r:
            # 将子节点的目的地和价格加入列表中
            for ndest, nprice in d[dest]:
                if price + nprice < r:
                    choices.append(
                        (ndest, price+nprice, stop-1))
    # end snippet dst
    # start snippet return
    if r == float("inf"):
        return -1
    else:
        return r
    # end snippet return
