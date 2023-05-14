class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()

        n = len(salary)
        salary = salary[1:n-1]

        return sum(salary) / len(salary)