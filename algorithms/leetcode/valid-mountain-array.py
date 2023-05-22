class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
      n = len(arr)
      cur = 0

      while cur + 1 < n and arr[cur] < arr[cur + 1]:
        cur += 1

      if cur == 0 or cur == n - 1:
        return False

      while cur + 1 < n and arr[cur] > arr[cur + 1]:
        cur += 1

      return cur == n - 1