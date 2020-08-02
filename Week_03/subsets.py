import copy
class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         #在原有集合的基础上加上新元素，再与原有集合相加
#         ans_list = [[]]
#         for l in range(len(nums)):
#             now_list = copy.deepcopy(ans_list)
#             for tmp in now_list:
#                 tmp.append(nums[l])
#             ans_list += now_list

#         return ans_list

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        self.nums = nums
        self.n = len(nums)
        self.ans = []
        self.tmp = []
        if self.n  < 1:
            return [[]]
        self.DFS(0, self.nums[0])
        self.tmp.pop()
        self.DFS(0)
        return self.ans


    def DFS(self, index, num=None):

        if num is not None:
            self.tmp.append(num)

        index += 1

        if index > self.n - 1:
            # print(self.tmp)
            self.ans.append(self.tmp.copy())
            return

        self.DFS(index, self.nums[index])
        # print(self.tmp)
        self.tmp.pop()
        self.DFS(index)
