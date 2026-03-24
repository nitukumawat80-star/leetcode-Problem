class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lists = []
        for num in nums:
            if num not in lists:
                lists.append(num)
        for i in range(len(lists)):
            nums[i] = lists[i]
        return len(lists)