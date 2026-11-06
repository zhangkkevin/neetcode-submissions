class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}':'{', ']':'[', ')':'('}
        l = []

        for p in s:
            if p in mapping.values():
                l.append(p)
            else:
                if len(l) > 0 and mapping[p] == l[-1]:
                    l.pop()
                else:
                    return False
        
        return not l