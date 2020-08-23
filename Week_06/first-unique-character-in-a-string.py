class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for i in s:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        for key, value in enumerate(s):
            if hash_map[value] == 1:
                return key

        return -1
