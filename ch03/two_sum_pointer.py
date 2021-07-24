from typing import List


# start snippet wow
def two_sum(nums: List[int], target: int) -> List[int]:
    i, j = 0, len(nums) - 1
    while i < j:
        if (s := nums[i] + nums[j]) == target:
            return [i, j]
        elif s > target:
            j -= 1
        else:
            i += 1
    return []
# end snippet wow


if __name__ == "__main__":
    two_sum([1, 3, 5, 7, 10], 12)
