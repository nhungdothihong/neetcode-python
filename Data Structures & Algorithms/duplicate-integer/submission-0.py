class Solution:
    def hasDuplicate(self, nums: list[int]):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False