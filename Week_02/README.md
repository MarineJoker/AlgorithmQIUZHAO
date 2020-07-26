### 学习笔记
这周主要是堆、树、递归的学习
这几个概念都互有相关性质，一句话总结就如下：  
堆是一颗完全二叉树，其父节点均比左孩子、右孩子大或者小，如此的递归下去就是一个最大堆或是最小堆  

### 注意的点：
递归最不要进行人肉递归，在做题之前先找到题目的最近重复子问题，想清楚再动手才事半功倍，以下面的全排列的题目为例子  
链接：https://leetcode-cn.com/problems/permutations/

读完题目我就按照以下思路进行思考:  
1、怎么暴力？
暴力for循环？看起来几个数字几个循环的节奏，明显不对；  
2、递归？
想到直接DFS，重复子问题:选择一个元素后在剩下的集合中继续选元素出来排列，该递归的重复逻辑就被分析出来了；  

坑:  
没有进一步分析是属于哪一种特点的递归，直接就开写了，以至于写了大半个钟在leetcode页面print进行debug，途中发现数据结构用的不合理又继续改，最后AC的代码就是如下的挫解；  
反思:  
该问题其实进一步分析就是最后的树的前序遍历，输出所有根到叶子节点的路径，利用回溯的形式能够更好地进行答案的存储，而我由于之前没有继续往下分析，直接开写了，导致一开是没有利用回溯，数据结构写的奇葩，debug了大部分时间，但由于已经想到方案了，就不想直接翻题解，最后的挫解也是偷懒利用了浅拷贝，没有想到官方解的swap方法，虽然最后得到解的空间复杂度差不多，但是再求解的过程中浪费了很多内存；  
问题:  
像是这种已经想到解法，觉得自己能写出来的，但是debug了半个钟的行为是不是不如在觉得debug费劲的情况下直接翻题解？

```python
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
```
