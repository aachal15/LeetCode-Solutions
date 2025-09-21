class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum , rightsum = 0,sum(nums)

        for index,ele in enumerate(nums):
            rightsum -= ele
            if leftsum == rightsum:
                return index
            leftsum += ele
        return -1
