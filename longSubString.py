class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # if (len(s) == 0): return 0
        l, r, longest = 0, 0, 0

        uni = {}
        while r < len(s):
            
            if (s[r] not in uni):

                uni[s[r]] = r

                r += 1

                if r - l > longest:
                    longest = r - l
            else:
                l = uni[s[r]] + 1
                r = l
                uni = {}
            
            
        return longest

print(Solution.lengthOfLongestSubstring(0, "abcabcbb"))