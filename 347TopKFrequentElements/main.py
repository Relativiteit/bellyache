from typing import List
nums: List[int] = [4,4,1, 1, 1, 2, 2, 3]
k: int = 2


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count elements in list 
        number_table = {}
        # print(number_table)
        for i in nums:
            if i in number_table:
                number_table[i] += 1
                # print(number_table)
            else:
                number_table[i] = 1
                # print(number_table)

        sorted_items = sorted(number_table.items(),  key= lambda x: x[1], reverse=True )
        print(sorted_items)

        # count amount of values in values of key: value paris 
        most_frequent = [sorted_items[i][0] for i in range(k)]
        return most_frequent

if __name__ == "__main__":
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    print(result)
