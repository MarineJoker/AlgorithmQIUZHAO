class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {'{': '}', '(': ')', '[': ']', '':''}
        stack = []
        # 栈
        for tmp in s:
            if len(stack)!=0 and map_dict[stack[-1]] == tmp:
                stack.pop()
            elif tmp not in map_dict:
                return False
            else:
                stack.append(tmp)
        if len(stack)>0 and ''.join(stack)!='':
            return False
        return True
