class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=defaultdict(int)
        loser=defaultdict(int)
        players=set()
        res=[[],[]]
        for arr in matches:
            winner[arr[0]]+=1
            loser[arr[1]]+=1
            players.add(arr[0])
            players.add(arr[1])
        for i in players:
            if i in winner and i not in loser:
                res[0].append(i)
            elif loser[i] == 1:
                res[1].append(i)
        res[0].sort()
        res[1].sort()
        return (res)