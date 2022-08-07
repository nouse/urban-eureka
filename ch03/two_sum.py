from typing import List, Dict


# start snippet wow
def two_sum(nums: List[int], target: int) -> List[int]:
    """
        >>> two_sum([7, 2, 1, -1], 6)
        [0, 3]
    """
    d: Dict[int, int] = {}
    for i, n in enumerate(nums):
        if n in d:
            return [d[n], i]
        d[target - n] = i
    return []
# end snippet wow
