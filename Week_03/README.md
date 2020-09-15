## 学习笔记

### 二分查找旋转数组的思考

**问:** 为什旋转后依然能进行二分查找？  
**答:** 因为为二分查找的本质是筛选掉一半的值，而虽然数组进行了旋转，    
但我们依然可以发现进行二分后不含转折点的部分定是有序的，  
而根据有序的那部分数据就可得知所找的值在哪一部分，所以同样达到了二分的效果，  
至于找转折点，也就是找最小值，那么终止条件就可设为当 mid>mid+1 mid则为转折点也为最小值  

### 二分查找的两种模板总结

```python
# 传统二分，在左右闭区间里搜索
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <=right:     # left == right + 1终止 [right+1, right]
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1

# 最左侧，左闭右开写法[)
# [1,2,2,2,2,2]
def binary_search(nums, target):
    left, right = 0, len(nums)
    while left < right:    # left == right终止[left, left)
        mid = (left+right)//2
        if nums[mid] == target:
            right = mid
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
    return left
```
# 注意左侧边界实际意思是小于查找的数在区间有多少个
例： [1,2]找3时，返回2，实际上就是没找到  
题目相关：x的平方根，早餐组合(利用二分查找加速)  
