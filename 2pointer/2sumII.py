from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        step = 0
        output = []

        while (l < r):
            print('l:', l)
            print('r:', r)

            if (numbers[l] + numbers[r] == target):
                output.append([numbers[l], numbers[r]])
                l += 1
                r = r - 1
            else: 
                if (numbers[l] + numbers[r] < target):
                    l+= 1
                else:
                    r = r - 1
                step += 1
        return output

print(Solution().twoSum([1,2,3,4], 5))