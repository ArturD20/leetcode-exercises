class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        
        n = len(jewels)
        ans = 0
        typeOfJewels = []
        for char in jewels:
            typeOfJewels.append(char)
        for jewel in typeOfJewels:
            ans += stones.count(jewel)
        
        return ans


        