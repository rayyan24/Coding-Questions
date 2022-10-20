from math import sqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # a=[1]*n
        # counter=1
        # for i in range(len(a)):
        #     if i%2!=0:
        #         a[i]=0
        # counter=2
        # print(a)
        # for i in range(len(a)):
        #     if i%3!=0:
        #         if a[i]==0:
        #             a[i]==1
        #         else:
        #             a[i]=0
        # counter=4
        # print(a)
        # while counter<n:
        #     for i in range(len(a)):
        #         if i%counter!=0:
        #             if a[i]==0:
        #                 a[i]==1
        #             else:
        #                 a[i]=0
        #     counter+=1
        # if a[-1]==0:
        #     a[-1]==1
        # else:
        #     a[-1]=0
        # print(a)
        return int(sqrt(n))
