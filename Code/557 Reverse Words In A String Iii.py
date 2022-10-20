class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        revWords = [word[::-1] for word in s]
        return " ".join(revWords)
