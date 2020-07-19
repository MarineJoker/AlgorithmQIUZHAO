#两边往中间依次收敛，需求更高的区域
#宽已经是最宽了，接下来就是要找在更高的里面有没有更优的解(如何构造更高的解?)
#解法主要过程就是如何找到更高的，最小的动，因为面积取决于最小的那根

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_are = 0
        j = n-1
        i = 0
        for _ in range(n-1):
            if height[i] > height[j]:
                max_are = max(height[j]*(j-i), max_are)
                j -= 1
            else:
                max_are = max(height[i]*(j-i), max_are)
                i += 1
            if j <= i:
                return max_are
