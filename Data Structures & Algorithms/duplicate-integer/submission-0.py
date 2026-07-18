class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            a.add(i)

        if len(a) == len(nums):
            return False
        else:
            return True