class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1.对字符串排序
        # 2.排序后哈希
        # {'key': index} 唯一值做key映射到列表的index上

        map_dict = {}
        ans_list = []
        index = -1
        for tmp in strs:
            key = ''.join(sorted(tmp))
            if key not in map_dict:
                index += 1
                map_dict[key] = index
                ans_list.append([tmp])
            else:
                ans_list[map_dict[key]].append(tmp)

        return ans_list
