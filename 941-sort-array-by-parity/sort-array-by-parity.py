class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        count=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[count],nums[i]=nums[i],nums[count]
                count+=1
        return nums

        