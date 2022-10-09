class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows,Columns=len(board),len(board[0])
        path=set()
        
        def helper(row,col,indCurChar):
            if indCurChar==len(word):
                return True
            if row<0 or col<0 or row>=Rows or col>=Columns or word[indCurChar]!=board[row][col] or (row,col) in path:
                return False
            path.add((row,col))
            # checking for every adjacent row and column
            temp=helper(row+1,col,indCurChar+1) or helper(row-1,col,indCurChar+1) or helper(row,col+1,indCurChar+1) or helper(row,col-1,indCurChar+1) 
            path.remove((row,col))
            return temp
                # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        for r in range(Rows):
            for c in range(Columns):
                if helper(r,c,0) ==True:
                    return True
        return False
                