from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = 0
        output = []
        if len(nums) < 3: return []
        nums.sort()
        while (a <= len(nums) - 3):
            l, r = a + 1, len(nums) - 1

            while (l < r): 
                sum = nums[a] + nums[l] + nums[r]

                if (sum == 0): 
                    dup = False
                    for n in nums:
                        if n == [nums[a], nums[l], nums[r]]: dup = True
                    
                    if (dup == False): output.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r = r - 1

                elif (sum > 0):
                    r = r - 1
                else:
                    l += 1
            a += 1
        return output
                

print(Solution().threeSum([-1,0,1,2,-1,-4]))
        



