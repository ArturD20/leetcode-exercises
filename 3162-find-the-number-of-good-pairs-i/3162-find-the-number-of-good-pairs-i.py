class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        
        gp = 0
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            for j in range(m):
                if nums1[i] % (nums2[j] * k) == 0:
                    gp += 1

        return gp
        