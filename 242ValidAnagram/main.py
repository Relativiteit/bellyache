s: str = "anagram"
t: str = "nagaram"
d: str = "car"
e: str = "dog"


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # check for same length
            print('not same length')
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            print("true")
            return True
        else:
            print("false")
            return False


if __name__ == "__main__":
    solution = Solution()
    solution.isAnagram(s, t)
