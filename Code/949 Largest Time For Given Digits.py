class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        result = ""
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if i == j or j == k or i == k:
                        continue
                    hours = str(arr[i])+str(arr[j])
                    mins = str(arr[k])+str(arr[6-i-j-k])
                    time = hours+":"+mins
                    if hours < "24" and mins < "60" and time > result:
                        result = time
        return result
