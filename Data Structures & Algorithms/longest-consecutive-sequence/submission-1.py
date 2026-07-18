class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k = set(nums)
        count = 0
        for i in k:
            if (i-1) not in k:
                l = 1
                while (i+l) in k:
                    l+=1
                count = max(l, count)

        return count
