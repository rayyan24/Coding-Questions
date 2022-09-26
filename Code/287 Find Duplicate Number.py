class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = arr[slow]
            slow2 = arr[slow2]
            if slow == slow2:
                return slow


class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
#         do not init hare to the starting keep it where it is
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
