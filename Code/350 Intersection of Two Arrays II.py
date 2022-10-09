class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # from collections import defaultdict
        # Map={}
        # size1=len(arr1)
        # size2=len(arr2)
        # for i in arr1:
        #         if i in arr2:
        #             if i in Map:
        #                 Map[i]+=1
        #             else:
        #                 Map[i]=1
        # res=[]
        # '''
        # elem[0]--> element
        # elem[1]--> count
        # '''
        # for elem in Map.items():
        #     for _ in range(elem[1]):
        #         res.append(elem[0])
        # return (res)
                    # Output that we want to return
        output = []
            
            # To keep the count of each element in nums2
        count = Counter(nums2)
            
            # Now for each element in first array
        for num in nums1:
                # If count of that element is > 0 we can include it
            if num in count and count[num] > 0:
                output.append(num)
    # Reduce its count by 1 as we included this element once in the output
                count[num] -= 1
        return output