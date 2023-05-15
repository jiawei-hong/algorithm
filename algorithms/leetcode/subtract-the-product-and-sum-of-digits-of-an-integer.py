class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_of_nums = sum(map(lambda x: int(x), list(str(n))))
        times_of_nums = reduce(lambda x,y: x * y, map(lambda x:int(x), list(str(n))))
        
        return times_of_nums - sum_of_nums