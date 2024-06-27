class Solution(object):
    def isPalindrome(self, x):
        
        s = str(x)
        reversedS = s[::-1]
        if reversedS == s:
            return True
        else:
            return False