class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
# [2],
# [3,4],
# [6,5,7],
# [4,1,8,3]
# 模拟二叉数深度优先搜索(后续缓存父节点得到的最小值)
        mem_dict = {}
        def dfs(depth, index):
            if depth == len(triangle):
                return 0
            if (depth,index) in mem_dict.keys():
                return mem_dict[(depth,index)]
            mem_dict[(depth, index)] = min(dfs(depth+1,index), dfs(depth+1,index+1))+triangle[depth][index]
            return mem_dict[(depth, index)]
        return dfs(0, 0)
