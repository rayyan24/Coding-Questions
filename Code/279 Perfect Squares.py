class Solution:
    def numSquares(self, n) -> None:
        if n < 2:
            return n
        squares = []
        i = 1
        while i * i <= n:
            squares.append( i * i )
            i += 1
        count = 0
        toCheck = {n}
        while toCheck:
            count += 1
            temp = set()
            for curElem in toCheck:
                for square in squares:
                    if curElem == square:
                        return count
                    if curElem < square:
                        break
                    temp.add(curElem-square)
            toCheck = temp



class Solution:
    def numSquares(self, n) -> None:
        if n < 2:
            return n
        squares = []
        i = 1
        while i * i <= n:
            squares.append( i * i )
            i += 1
        print(squares)
        count = 0
        toCheck = {n}
        print(toCheck)
        while toCheck:
            count += 1
            temp = set()
            for curElem in toCheck:
                for square in squares:
                    if curElem == square:
                        return count
                    if curElem < square:
                        break
                    temp.add(curElem-square)
            toCheck = temp
            print(toCheck)

def main() -> None:
    object=Solution()
    res=object.numSquares(12)
    print(res)
if __name__=="__main__":
    main()