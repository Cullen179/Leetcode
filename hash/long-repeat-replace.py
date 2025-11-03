# 424. Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        l = 0
        maxFre = s[0]
        map={}
        for r in range(len(s)):
            if (map.get(s[r]) is None):
                map[s[r]] = 1
            else:
                map[s[r]] += 1

            if r - map[maxFre] - l + 1 > k:
                map[s[l]] -= 1
                l += 1 


            if s[r] != maxFre and map[s[r]] >= map[maxFre]:
                maxFre = s[r]
                
            if longest < r - l + 1: longest = r - l + 1

        return longest
print(Solution().characterReplacement('DPDPFP', 2))

# r - map[maxFre] + 1 > k:


                
