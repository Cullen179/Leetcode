# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        l = 0
        maxL = 0

        for r in range(0, len(s)):
            if (hashMap.get(s[r])) is None:
                hashMap[s[r]] = r
            else:
                if l < hashMap.get(s[r]) + 1: l = hashMap.get(s[r]) + 1
                hashMap[s[r]] = r
            
            if (r - l + 1 > maxL) : maxL = r - l + 1

        return maxL
    
print(Solution().lengthOfLongestSubstring('tmmzuxt'))
print(Solution().lengthOfLongestSubstring('bbbbb'))

            