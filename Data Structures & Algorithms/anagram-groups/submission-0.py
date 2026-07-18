class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = {}
        ans  = []
        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str in l:
                l[sorted_str].append(i)
            else:
                l[sorted_str] = [i]

        for i in l:
            ans.append(l[i])

        return ans
        