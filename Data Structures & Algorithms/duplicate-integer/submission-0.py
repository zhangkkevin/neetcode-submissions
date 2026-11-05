class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            else:
                return True
        
        return False