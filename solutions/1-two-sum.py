from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return run2(nums, target)


# Two pass solution
def run1(nums: List[int], target: int) -> List[int]:
    idx = {}
    for i, n in enumerate(nums):
        # NOTE for future me:
        # in case when multiple equal values are present in list
        # this value will be mapped to the last index of occurrence
        # e.g. [3,3,3] -> idx[3] = 2
        idx[n] = i
    for i_n, n in enumerate(nums):
        # target = comp + n ->
        comp = target - n
        i_comp = idx.get(comp)
        # `comp` might not be mapped to its index in given list
        # but if if does... (and it's not the same value `n`)
        if i_comp != None and i_comp != i_n:
            # ... than we found the solution
            return [i_n, i_comp]
    return []


# One pass solution
def run2(nums: List[int], target: int) -> List[int]:
    idx = {}
    # NOTE for future me:
    # In one pass solution we only look backward for the solution
    # (aka values which were added before current value).
    # We don't need to bother looking forward, because
    # it is the problem of the future value to, again, look backward.
    # so for [2, 7, 11, 15] and target=9,
    # when we add 2 and can't find target-2=7 in dict --- not a problemo
    # because when we add 7 the target-7=2 will be found.
    for i, n in enumerate(nums):
        comp = target - n
        i_comp = idx.get(comp)
        idx[n] = i
        if i_comp != None and i_comp != i:
            return [i_comp, i]
    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    # nums = [3, 2, 4]
    # target = 6
    # nums = [3, 3]
    # target = 6
    sol = Solution()
    print(sol.twoSum(nums, target))
