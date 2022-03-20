class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count_map = {}
        res = []
        length = len(nums)//3
        for i in nums:
            if i in count_map:
                count_map[i] += 1
            else:
                count_map[i] = 1

        for key in count_map.keys():
            if count_map.get(key) > length:
                res.append(key)

        return res