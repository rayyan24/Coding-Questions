class Solution:
    def canConstruct(self, toBuild: str, availableChars: str) -> bool:
        if len(availableChars) < len(toBuild):
            return False
        AC = [i for i in availableChars]
        for i in toBuild:
            if i in AC:
                AC.remove(i)
                continue
            else:
                return False
        return True
