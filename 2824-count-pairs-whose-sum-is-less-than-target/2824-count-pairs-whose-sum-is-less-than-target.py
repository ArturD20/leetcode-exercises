class Solution(object):
    def countPairs(self, nums, target):
        
        length = len(nums)
        i = 0
        j = 0
        pairs = 0

        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                elif i < j and (nums[i] + nums[j]) < target:
                    pairs += 1
        return pairs
                    
        