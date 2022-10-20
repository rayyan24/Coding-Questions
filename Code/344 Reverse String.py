class Solution:
    def reverseString(self, s: List[str]) -> None:
        s1 = s[::-1]
        print(s1)
        for i in range(len(s)):
            s[i] = s1[i]
