class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefNum = 0
        for word in words:
            if word.startswith(pref):
                prefNum += 1 
        return prefNum