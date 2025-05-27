from typing import List

nums: List[int] = [1, 2, 3, 1]


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True


if __name__ == "__main__":
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)

    test_date = [1, 3, 4, 5]
    assert solution.containsDuplicate(test_date) == False
    test_date = [1, 1, 2, 4, 5]
    assert solution.containsDuplicate(test_date) == True
    test_neg = [-1, -2, -3, -4]
    assert solution.containsDuplicate(test_neg) == False
    assert solution.containsDuplicate([]) == False
