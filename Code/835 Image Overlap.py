'''
835 Image Overlap
Medium
You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.
We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.
Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.
Return the largest possible overlap.
'''
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]):
        d = collections.defaultdict(int) # returns 0 insted of index error
        a = []
        b = []     
        n=len(A)
        ans = 0
#       adding all the indexes which have 1 into a list for both matrices
#       tuples are indexable
        for i in range(n):
            for j in range(n):
                if(A[i][j] == 1):
                    a.append((i,j))
                if(B[i][j] == 1):
                    b.append((i,j))
#        t1,t2 are tuples t[0] is row t[1] is column where there is a zero
        for t1 in a:
            for t2 in b:
                t3 = (t2[0]-t1[0],t2[1]-t1[1])
                d[t3] += 1
                ans = max(ans, d[t3])
        return ans 
        