class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = res = 0
        heap = []
        paris = zip(nums1, nums2)
        sorted_pairs = sorted(paris, key=lambda x: x[1],reverse=True)

        for num1,num2 in sorted_pairs:
            n = len(heap)
            heappush(heap, num1)
            total += num1

            if n > k:
                total -= heappop(heap)

            if n == k:
                res = max(res, total * num2)

        return res