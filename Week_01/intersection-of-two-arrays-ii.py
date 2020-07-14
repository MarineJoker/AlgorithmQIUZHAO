class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 遍历列表存在的放入dict，同时存在的元素则为交集
        map_dict = {}
        self.ans_list = []
        self.check(map_dict, nums1, 'add')
        self.check(map_dict, nums2, 'union')
        return self.ans_list

    def check(self, map_dict, nums, option):
        if option == 'add':
            for num in nums:
                if num in map_dict:
                    map_dict[num] += 1
                else:
                    map_dict[num] = 1
        else:
            for num in nums:
                if num in map_dict and map_dict[num] > 0:
                    map_dict[num] -=1
                    self.ans_list.append(num)
