class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)

        if n == 2:
            return True

        diff = abs(arr[0] - arr[1])

        for i in range(2, n):
            if abs(arr[i] - arr[i-1]) != diff:
                return False

        return True
