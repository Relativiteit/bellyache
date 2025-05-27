from typing import List

nums: List[int] = [2, 7, 11, 15]
target: int = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in dictionary:
                return ([dictionary[difference], index])
            dictionary[value] = index


if __name__ == "__main__":
    solution = Solution()
    solution.twoSum(nums, target)

    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
