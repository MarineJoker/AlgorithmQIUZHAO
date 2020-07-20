# 自己回忆到两数之合想到的6行解决
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        check = {}
        for key, val in enumerate(numbers):
            if target - val in check: return ([check[target - val]+1, key+1])
            check[val] = key
