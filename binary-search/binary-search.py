# 704. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

import math


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        m = int(len(nums) / 2)
        l, r = 0, len(nums) - 1
        
        if (nums[l] == target): return 0
        if (nums[r] == target): return r
        
        # what if don't find target
        while (m != l and m != r):
            if nums[m] == target:
                return m
            
            if (nums[m] < target):
                l = m
                m = math.floor((m + r) / 2)
            else:
                r = m
                m = math.ceil((l + r) / 2)
                
        
        return -1
    
print(Solution().search([-1,0,3,5,9,12], 2))