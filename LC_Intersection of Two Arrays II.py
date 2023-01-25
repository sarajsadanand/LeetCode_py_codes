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

# Second approach using pointers
class Solution1:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        res = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1

        return res
                    
obj1 = Solution1()
obj1.intersect(nums1, nums2)