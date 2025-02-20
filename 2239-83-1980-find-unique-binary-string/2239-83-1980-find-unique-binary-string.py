class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        i = 0
        for num in nums:
            if num[i] == "0":
                res.append("1")
            else:
                res.append("0")
            i += 1

        return "".join(res)