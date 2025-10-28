# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) < k: return 0
        a = k
        largest = 0
        while (a < len(nums) - 1):
            total = nums[a - k + 1]
            for n in range(0, k - 1):
                total += nums[a - n]
            if (total / k > largest): largest = total/k
            a += 1

        return largest
        
print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))