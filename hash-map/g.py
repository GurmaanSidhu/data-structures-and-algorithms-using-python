# time took - 3ms
# Beats - 99.72%


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        m_len = 0
        map1 = {}
        for right, element in enumerate(s):
            if element in map1 and map1[element] >= left:
                left =  map1[element] + 1
            map1[element] = right
            m_len = max(m_len, right-left+1)
        
        return m_len