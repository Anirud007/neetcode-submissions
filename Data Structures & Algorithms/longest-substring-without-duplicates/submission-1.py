class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        ml = 0
        count = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in hs:
                hs.add(s[r])
                count += 1
                r += 1
                ml = max(count, ml)
            else:
                hs.discard(s[l])
                l += 1
                count  -= 1

        return ml

            
            