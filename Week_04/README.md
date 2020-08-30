###学习笔记
#### 动态规划相关变形  
乘积为正数的最长子数组长度  https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product/  
乘积最大子数组  https://leetcode-cn.com/problems/maximum-product-subarray/  
乘积为正数的最长子数组长度 动态规划求解  
dp[n][0] 以n结尾的最大长度正整数子串  
dp[n][1] 以n结尾的最大长度负数子串  
```python
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0,0] for _ in range(n+1)]
        dp[0][0] = 0
        dp[0][1] = 0
        anw = 0
        for i in range(1, n+1):
            if nums[i-1] == 0:
                dp[i][0] = 0
                dp[i][1] = 0
            elif nums[i-1] > 0:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = (dp[i-1][1] + 1) if dp[i-1][1] else 0
            else:
                dp[i][0] = (dp[i-1][1] + 1) if dp[i-1][1] else 0
                dp[i][1] = dp[i-1][0] + 1
            anw = max(anw, dp[i][0])
        return anw;


```
