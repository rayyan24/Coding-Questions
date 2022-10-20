class Solution:
    def average(self, salary: List[int]) -> float:
        # Sum=sum(salary)-min(salary)-max(salary)
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)
