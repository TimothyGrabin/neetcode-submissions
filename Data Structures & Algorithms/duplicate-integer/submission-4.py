class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for num in nums:
            new_set.add(num)
        i = 0
        for number in new_set: 
            i += 1
        j = 0
        for num in nums:
            j += 1
        return(not(i == j))