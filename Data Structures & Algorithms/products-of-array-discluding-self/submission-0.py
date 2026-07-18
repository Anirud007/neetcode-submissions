class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) - 1
        i = 1
        s = [0] * (n+1)
        p = [0] * (n+1)
        p[0] = 1
        s[n] = 1
        while i <= n:
            p[i] = p[i-1] * nums[i-1]
            i+=1 

        j = n-1
        while j >= 0:
            s[j] = s[j+1] * nums[j+1]
            j-=1

        ans = [0]*(n+1)
        for i in range(len(ans)):
            ans[i] = s[i]*p[i]

        return ans

            