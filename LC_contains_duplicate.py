nums = [3,1,2,4,2,9]
class Solution:
    def containsDuplicate(self, nums):
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                return True
        return False

item = Solution()
item.containsDuplicate(nums)