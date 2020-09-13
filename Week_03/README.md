## 学习笔记

### 二分查找旋转数组的思考

**问:** 为什旋转后依然能进行二分查找？  
**答:** 因为为二分查找的本质是筛选掉一半的值，而虽然数组进行了旋转，    
但我们依然可以发现进行二分后不含转折点的部分定是有序的，  
而根据有序的那部分数据就可得知所找的值在哪一部分，所以同样达到了二分的效果，  
至于找转折点，也就是找最小值，那么终止条件就可设为当 mid>mid+1 mid则为转折点也为最小值  

```python
class Solution(object):
    def mySqrt(self, x):
        # 取最小符合要求的二分查找模板
        left, right = 1, x 
        # [left, right]
        while left <= right:
            mid = (left + right)// 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1
        return left -1
```
题目相关：x的平方根，早餐组合(利用二分查找加速)  
