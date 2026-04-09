class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = len(nums)
        seen = set()
        status = False
        for n in nums:
            if n in seen:
                status = True
            seen.add(n)
        return status