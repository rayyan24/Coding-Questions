class Solution:
    def merge(self, nums1: List[int], l1: int, nums2: List[int], l2) -> None:
        last = l1+l2-1
        while l1 > 0 and l2 > 0:
            if nums1[l1-1] > nums2[l2-1]:
                nums1[last] = nums1[l1-1]
                l1 -= 1
            else:
                nums1[last] = nums2[l2-1]
                l2 -= 1
            last -= 1
        while l2 > 0:
            nums1[last] = nums2[l2-1]
            last -= 1
            l2 -= 1
