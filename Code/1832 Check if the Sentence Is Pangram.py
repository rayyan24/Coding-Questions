class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr=[0]*26
        for char in sentence:
            arr[ord(char)-97]=1
        for i in arr:
            if i==0:
                return False
        return True