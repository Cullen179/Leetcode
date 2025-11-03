# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        l, r = 0, 0
        sum = 0
        totalSub = 0
        # nums.sort()
        while (l <= r and r < len(nums)):            
            
            if (sum >= k):
                sum = sum - nums[l]
            else:
                sum += nums[r]                    
                r += 1

            if (sum == k):
                totalSub += 1
                sum = sum - nums[l]
                l+= 1
            
        return totalSub

print(Solution().subarraySum([1,2,3], 3))
                