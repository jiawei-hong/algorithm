class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res,lis = [],[]

        for obstacle in obstacles:
            i = bisect.bisect_right(lis, obstacle)

            if i == len(lis):
                lis.append(obstacle)
            else:
                lis[i] = obstacle
            
            res.append(i+1)
        return res