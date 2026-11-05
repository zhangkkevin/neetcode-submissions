class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for s_char in s:
            if s_char not in d:
                d[s_char] = 1
            else: 
                d[s_char] += 1
        
        for t_char in t:
            if t_char not in d:
                d[t_char] = -1
            else:
                d[t_char] -= 1
        
        return all(count == 0 for count in d.values())
        