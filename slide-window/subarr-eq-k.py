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
        # don't affect since if count plus before the the sum in dict update
        sum = {0: 1}
        curSum = 0
        count = 0
        for n in range(len(nums)):
            curSum += nums[n]
            # if previous sum[cur - k] exists
            if (not (sum.get(curSum - k) is None)):
                count += sum[curSum - k]

            if (sum.get(curSum) is None):
                sum[curSum] = 1
            else:
                sum[curSum] += 1


        return count

print(Solution().subarraySum([0, 0, 0], 0))


               
