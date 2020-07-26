import copy
class Solution:
    # 思路是看题目就有，但是写了半个多钟的挫解
    def permute(self, nums: List[int]) -> List[List[int]]:
        #可以用深搜
        self.ans = []
        n = len(nums)
        self.index = 0
        nums_set = set(nums)
        self.DFS(nums_set, [])
        return self.ans

    def DFS(self, List ,ans):
        n = len(List)
        # print(n)
        if not n:
            self.ans.append(ans.copy())
            return

        for index in range(n):
            ans.append(List[index])
            List_tmp = List.copy()
            List_tmp.pop(index)
            self.DFS(List_tmp, ans)
            ans.pop()
    # 官方解
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res

