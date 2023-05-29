class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        record = {}
        
        for i in range(n):
            arr = list(set(nums[i]))
            
            for num in arr:
                if num in record:
                    record[num] += 1
                else:
                    record[num] = 1

        res = []
        
        for k,v in record.items():
            if v == n:
                res.append(k)
        res.sort()
        return res