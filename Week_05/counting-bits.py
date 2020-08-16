class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0 for _ in range(num+1)]
        for i in range(1, num+1):
            bits[i] += bits[i & (i - 1)] + 1

        return bits
