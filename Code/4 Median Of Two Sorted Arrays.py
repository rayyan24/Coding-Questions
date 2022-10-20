class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        size1, size2 = len(A), len(B)
#         this ensures that arr1 is always the smaller array
        if size1 > size2:
            A, B = B, A
            size1, size2 = size2, size1
        left = 0
        right = size1-1
        total = size1+size2
        half = total//2
        while True:
            # i--> mid pointer for A
            # j--> mid pointer for B
            i = (left+right)//2
#           -2 in order to adust with zero based indexing of both the arrays
            j = half-i-2
            # left partition ka last element of A
            Aleft = A[i] if i >= 0 else float("-infinity")
            # right partition ka first element of A
            Aright = A[i+1] if (i+1) < size1 else float("infinity")
            # left partition ka last element of B
            Bleft = B[j] if j >= 0 else float("-infinity")
            # right partition ka first element of B
            Bright = B[j+1] if (j+1) < size2 else float("infinity")
#             we got a correct partition for arrays
            if Aleft <= Bright and Bleft <= Aright:
                #                 odd
                if total % 2:
                    return min(Aright, Bright)
#                 even
                else:
                    return (min(Aright, Bright)+max(Aleft, Bleft))/2
            elif Aleft > Bright:
                right = i-1
            else:
                left = i+1
        # return 0.2
