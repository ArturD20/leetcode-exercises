class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        res = defaultdict(int)

        for num in nums:
            res[num] += 1
            
        for num in nums:
            if res[num] % 2 == 1:
                return False
        
        return True