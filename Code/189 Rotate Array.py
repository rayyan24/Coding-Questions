class Solution:
    def reverse(self, a, lb, ub):

        while (lb < ub):
            a[lb], a[ub] = a[ub], a[lb]
            lb += 1
            ub -= 1

    def rotate(self, arr: List[int], k: int) -> None:
        k = k % len(arr)
        self.reverse(arr, 0, len(arr)-1)
        self.reverse(arr, 0, k-1)
        self.reverse(arr, k, len(arr)-1)
