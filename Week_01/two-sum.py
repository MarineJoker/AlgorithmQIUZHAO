# 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_map = {}
        index = 0
        for tmp in nums:
            v_k = target - tmp
            if v_k in d_map:
                return [d_map[v_k], index]
            d_map[tmp] = index
            index += 1

