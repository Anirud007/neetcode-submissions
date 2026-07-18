class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        maxf = 0
        ans  = 0
        l = 0
        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            maxf = max(maxf, hm[s[r]])
            
            ws = r - l + 1
            while ws - maxf > k:
                hm[s[l]] -= 1
                l += 1
                ws = r - l + 1

            ans = max(ans, ws)

        return ans