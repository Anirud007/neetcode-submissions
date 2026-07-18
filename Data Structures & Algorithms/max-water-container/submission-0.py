class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights) - 1
        i = 0
        j = len(heights) - 1
        m_s = 0
        while i < j:
            area = min(heights[i], heights[j]) * l
            m_s = max(m_s, area)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            l -= 1
            

        return m_s
        
        