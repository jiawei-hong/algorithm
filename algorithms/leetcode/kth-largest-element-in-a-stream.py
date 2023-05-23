class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.res = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        n = len(self.res)

        if n < self.k:
            heapq.heappush(self.res, val)
        elif val > self.res[0]:
            heapq.heapreplace(self.res, val)

        return self.res[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
