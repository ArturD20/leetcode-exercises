class Solution(object):
    def findPermutationDifference(self, s, t):
        
        dictS = {}
        dictT = {}
        length = len(s)
        permutation = 0

        for i in range(length):
            dictS[s[i]] = i
            dictT[t[i]] = i

        for letters in s:
            permutation += abs(dictT[letters] - dictS[letters])
        
        return permutation
            

    
        