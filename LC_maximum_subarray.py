class Solution:
    #def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums):

        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum = curSum + n
            maxSub = max(maxSub, curSum)
        
        return maxSub

nums = [-2,1,-3,4,-1,2,1,-5,4]
a = Solution()
a.maxSubArray(nums)