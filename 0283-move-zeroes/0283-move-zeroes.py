class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        res = [i for i in nums if i != 0]
        s = len(nums) - len(res)
        res.extend([0] * s)
        nums[:] = res
        return nums
        