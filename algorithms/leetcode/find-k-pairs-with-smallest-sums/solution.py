class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums1_n = len(nums1)
        nums2_n = len(nums2)

        if not nums1_n or not nums2_n:
            return []

        res = []
        q = []

        for i in range(nums1_n):
            heapq.heappush(q, (nums1[i] + nums2[0], i, 0))

        while len(res) < min(k, nums1_n * nums2_n):
            total, i, j = heapq.heappop(q)
            res.append([nums1[i], nums2[j]])

            if j + 1 < nums2_n:
                heapq.heappush(q, (nums1[i] + nums2[j + 1], i, j + 1))
        return res