# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         def is_palindrome(check):
#             return check == check[::-1]

#         words = {word: i for i, word in enumerate(words)}
#         valid_pals = []
#         for word, k in words.items():
#             n = len(word)
#             for j in range(n+1):
#                 pref = word[:j]
#                 suf = word[j:]
#                 if is_palindrome(pref):
#                     back = suf[::-1]
#                     if back != word and back in words:
#                         valid_pals.append([words[back],  k])
#                 if j != n and is_palindrome(suf):
#                     back = pref[::-1]
#                     if back != word and back in words:
#                         valid_pals.append([k, words[back]])
#         return valid_pals
class Solution:
    def palindromePairs(self, arr: List[str]) -> List[List[int]]:
        size = len(arr)
        ans = []
        for i in range(size):
            for j in range(i+1, size):
                concatStr1 = arr[i]+arr[j]
                concatStr2 = arr[j]+arr[i]
                if concatStr1 == concatStr1[::-1]:
                    ans.append([i, j])
                if concatStr2 == concatStr2[::-1]:
                    ans.append([j, i])

        return (ans)
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back],  k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals