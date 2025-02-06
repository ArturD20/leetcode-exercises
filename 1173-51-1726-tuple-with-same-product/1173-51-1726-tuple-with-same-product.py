class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        pair_count = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                pair_count[product] += product_count[product]
                product_count[product] += 1

        res = 0
        for cnt in pair_count.values():
            res += 8 * cnt

        return res
                