import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 先O(n)遍历一遍
        # 用哈希统计数量
        # 放入最小堆，pop掉多余的元素，剩下的就是高频词
        q = []
        map_count ={}
        ans = []
        for num in nums:
            if num in map_count:
                map_count[num] += 1
            else:
                map_count[num] = 0


        for key,val in map_count.items():
            heapq.heappush(q, (val, key))
            if len(q) > k:
                heapq.heappop(q)


        for _ in range(k):
            ans.append(heapq.heappop(q)[1])

        return ans
