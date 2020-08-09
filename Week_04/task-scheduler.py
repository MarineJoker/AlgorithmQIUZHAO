
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = [0 for _ in range(26)]
        for t in tasks:
            cnts[ord(t) - 65] += 1
        cnts.sort(reverse=True)
        if cnts[0] == 0:
            return 0
        ret = (cnts[0] - 1) * (n + 1) + 1
        remain = ret - cnts[0]
        for i in range(1, len(cnts)):
            if cnts[i] == cnts[0]:
                ret += 1
                remain -= cnts[i] - 1
            else:
                remain -= cnts[i]
            if remain <= 0:
                return len(tasks)
        return ret
