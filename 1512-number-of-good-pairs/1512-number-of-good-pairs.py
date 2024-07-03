from collections import Counter

class Solution(object):
    def numIdenticalPairs(self, nums):
        
        pairs = 0
        dictOfNums = Counter(nums)
        for value in dictOfNums.values():
            pairs += value * (value - 1) // 2
        
        return pairs
        
        
                    
        
        