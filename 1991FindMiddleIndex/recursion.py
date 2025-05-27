from typing import List 

nums: List[int] = [2,3,-1,8,4] 

class Solution:
    def findMiddleIndexRecursively(self, nums: List[int], index: int, global_value: int = None, left_total: int = 0) -> int:
        if global_value is None:
            global_value = sum(nums) # calculate sum of nums once 
        
        if index >= len(nums):
            return -1  # out of bounds 

        right_total = global_value - nums[index] - left_total

        if left_total == right_total:
            return index

        return self.findMiddleIndexRecursively(nums, index + 1, global_value, left_total + nums[index])

if __name__ == "__main__":
    solution = Solution()
    result = solution.findMiddleIndexRecursively(nums, 0)    
    print("middle index", result)