
from typing import List

# nums: List[int] = [2, 3, -1, 8, 4]
nums: List[int] = [-1,4,1,4]


class Solution:
    # Iterative approach
    def findMiddleIndex(self, nums: List[int]) -> int:
        global_value: int = sum(nums)
        left_total: int = 0
        result: int = 0 # to satisfy not having a middle index return -1 

        for index, value in enumerate(nums):
            right_total: int = global_value - value - left_total
            if left_total < right_total:
                print("left total < right total")
                left_total += value
            elif left_total > right_total:
                print("left total > right total")
                left_total += value
            elif left_total == right_total:
                result = index
                print("returning index", index)
                break

        return (result, "this is the result")


if __name__ == "__main__":
    solution = Solution()
    solution.findMiddleIndex(nums)
