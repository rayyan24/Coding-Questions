class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        count = {}
        freq = [[]for i in range(len(arr)+1)]
        for i in range(len(arr)):
            count[arr[i]] = 1+count.get(arr[i], 0)
        for value, cnt in count.items():
            freq[cnt].append(value)
        #  ith index of freq array is the number of elements that occur i times
        ans = []
        i = len(freq)-1
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                ans.append(j)
            if len(ans) == k:
                return (ans)
