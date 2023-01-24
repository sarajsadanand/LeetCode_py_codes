from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        if len(nums2) < len(nums1): return self.intersect(nums2, nums1)
            
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans


nums1 = [5,2,3,4,1]
nums2 = [7,3,4,6]

obj = Solution()
obj.intersect(nums1, nums2)