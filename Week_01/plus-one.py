from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 反向遍历
        digits = deque(digits)
        n = len(digits)
        for index in range(n-1, -1, -1):
            # print(index)
            add_val = digits[index] + 1
            if add_val > 9:
                digits[index] = 0
                if index == 0:
                    digits.appendleft(1)
            else:
                digits[index] = add_val
                break
        return list(digits)

