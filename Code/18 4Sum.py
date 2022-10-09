class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        size=len(arr)
        res=[]
        arr.sort()
        for i in range(size):
            for j in range(i+1,size):
                beg=j+1
                end=size-1
                subTarget=target-arr[i]-arr[j]
                while beg<end:
                    if arr[beg]+arr[end]<subTarget:
                        beg+=1
                    elif arr[beg]+arr[end]>subTarget:
                        end-=1
                    else:
                        # res.append([arr[i],arr[j],arr[beg],arr[end]])
                        res.append((arr[i],arr[j],arr[beg],arr[end]))
                        beg += 1
                        end -= 1
        return set(res)
                    