# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) < k: return 0
        a = k
        max = 0

        while (a <= len(nums) - 1):
          sum = nums[a]
          for n in range(1, k):
             sum += nums[a - n]
          
          if (sum / k > max): max = sum / k
          a += 1
        return max
            
        

print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
