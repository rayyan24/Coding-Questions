class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        Map = defaultdict(int)
        unpaired =0
        ans = 0
# The variable unpaired is used to store the number of unpaired words with both letters same. Unpaired here means a word that has not found its mirror word.At the end if unpaired same letter words are > 0, we can use one of them as the center of the palindromic string
        for curWord in words:
            # when  both the characters of curWord are same 
            if curWord[0] == curWord[1]:
                #when  both the characters of curWord are same and the curWord has already occored
                if Map[curWord] > 0:
                    unpaired -= 1
                    Map[curWord] -= 1
                    ans += 4
                # adding the current word to Map                 
                else: 
                    Map[curWord] += 1
                    unpaired += 1
            # when both the characters are different              
            else:
                revCurWord=curWord[::-1]
                # when both the characters are different and a reverse of current word is already present  
                if Map[revCurWord] > 0:  # w[::-1] -> reversed w
                    ans += 4
                    Map[revCurWord] -= 1
                else: Map[curWord] += 1
        if unpaired > 0: ans += 2
        return ans
        