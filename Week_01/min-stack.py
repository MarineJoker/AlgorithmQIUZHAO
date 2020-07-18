class MinStack:
    # 线性的话就要利用多一个栈去存当前栈内最小值
    # 由于栈先进后出的特性栈中每个元素可以用作保存从自身到内部的那个阶段的状态

    def __init__(self):
        # self.index = 0
        self.list = []
        self.heap = [float('inf')]
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:
        self.list.append(x)
        self.heap.append(min(x, self.getMin()))

    def pop(self) -> None:
        self.list.pop(-1)
        self.heap.pop(-1)

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.heap[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
