class Solution:
    def maxArea(self, arr: List[int]) -> int:
        size = len(arr)
        Max = 0
        # for i in range(size-1):
        #     for j in range(i+1,size):
        #         # getmin(arr[i],arr[j]) gives the length of rectangle
        #         # (j-i) gives the width of the rectangle
        #         # newMax=self.getmin(arr[i],arr[j])*(j-i)
        #         newMax=min(arr[i],arr[j])*(j-i)
        #         if newMax>max:
        #             max=newMax
        # return max
        low, high = 0, size-1
        while (low < high):
            # (high-low) gives length of rect
            # min(arr[high],arr[low]) gives width of rect
            area = (high-low)*min(arr[low], arr[high])
            Max = max(area, Max)
            if arr[low] < arr[high]:
                low += 1
            else:
                high -= 1
        return Max
