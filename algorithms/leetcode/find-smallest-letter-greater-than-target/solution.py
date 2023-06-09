class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n

        while l < r:
            mid = (l + r) // 2

            if letters[mid] > target:
                r -=  1
            else:
                l += 1

        return letters[l % n]
