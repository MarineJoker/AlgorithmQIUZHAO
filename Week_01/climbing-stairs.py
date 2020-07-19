#1.暴力误解，懵逼怎么破？
#2.找最近子问题
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2: return n
        a, b, temp = 1, 2, 0
        for i in range(3,n+1):
            temp = a + b
            a = b
            b = temp
        return temp


