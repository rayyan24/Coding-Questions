class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        s = list(s)
# i refers to every element of list and for every element it checks frequency of that element in hashmap and the actual current element like it compares ascii values of current char i.e i
        s.sort(key=lambda i: (cnt[i], i))
        return "".join(s)[::-1]
