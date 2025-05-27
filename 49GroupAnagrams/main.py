from typing import List
strs: List[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]

from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values)
    


if __name__ == "__main__":
    solution = Solution()
    solution.groupAnagrams(strs)
    assert solution.groupAnagrams(["goat", "toag", "otag", "tag", "gat"]) == [
        ["goat", "toag", "otag"], ["tag", "gat"]]
