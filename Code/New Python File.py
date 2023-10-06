class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(s) != len(pattern):
            return False
        wordToChar={}
        charToWord={}
        for char,word in zip(pattern,s):
            if char in charToWord and charToWord.get(char)!=word:
                return False
            if word in wordToChar and wordToChar.get(word)!=char:
                return False
            wordToChar[word]=char
            charToWord[char]=word
        return True
