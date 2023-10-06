words = ["cba",
         "daf",
         "ghi"]
cnt = 0
for col in range(len(words[0])):
    for row in range(len(words)-1):
        if words[row][col] > words[row+1][col]:
            cnt += 1
            break
print(cnt)


class Solution:
    def minDeletionSize(self, words: List[str]) -> int:
        cnt = 0
        for col in range(len(words[0])):
            for row in range(len(words)-1):
                if words[row][col] > words[row+1][col]:
                    cnt += 1
                    break
        return cnt
