from functools import lru_cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 分治
        # 如果N是偶数的话
        # 如果N是奇数的话
        if n == 0:
            return 1
        ans = self.deal(x, abs(n))
        if n<0:
            ans = 1/ans
        return ans

    @lru_cache
    def deal(self, x, n):
        if n == 1:
            return x
        elif n%2 == 0:
            return self.deal(x, n/2) * self.deal(x, n/2)
        else:
            return self.deal(x,(n - int(n/2))) * self.deal(x,int(n/2))
