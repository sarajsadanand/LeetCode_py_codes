class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
       
       # start merging from the ends of the lists
        p1, p2 = m-1, n-1
        # destination d index to insert into nums1
        for d in range(m+n-1, -1, -1):
            # if second list is empty, nothing more to merge
            if p2 < 0:
                return
            # only merge from nums1 if there are items left to merge
            # insert at d the larger of the two values from nums1 and nums2
            if p1 >= 0 and nums1[p1] > nums2[p2]:                
                nums1[d] = nums1[p1]
                p1 = p1 - 1
            else:
                nums1[d] = nums2[p2]
                p2 = p2 - 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

a = Solution()
a.merge(nums1, m, nums2, n)