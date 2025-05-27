from typing import List


def basic_test(word: str):
    i = 0
    n = len(word)
    result = (i + 1) % n

    print(result)


basic_test("gat")


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        print("goat")
