class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        tmp = nums[0]
        i = 0
        for _ in range(l-1):
            i += 1
            if nums[i] == tmp:
                del nums[i]
                i -= 1
            else:
                tmp = nums[i]
        return len(nums)
