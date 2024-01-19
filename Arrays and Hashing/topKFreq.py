class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        slis = sorted(map.items(), key=lambda item:item[1], reverse = True)

        for i in range(k):
            res.append(slis[i][0])
        return res