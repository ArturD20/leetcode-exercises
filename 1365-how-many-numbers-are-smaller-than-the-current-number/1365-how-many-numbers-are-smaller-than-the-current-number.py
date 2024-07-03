class Solution(object):
    def smallerNumbersThanCurrent(self, nums):

        n = len(nums)
        rArray = []
        for i in range(n):
            gp = 0
            for j in range(n):
                if nums[i] > nums[j] and i != j:
                    gp += 1
            rArray.append(gp)

        return rArray
    