# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# How to find which group to assign
    # make into string and find in map
    # initiate a [] and represent a word with its index of array group
# how to find if is anagram
    # how to count of new words only, keep old words
    # double check if all values is 0

# given map, how to return

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        out = []
        map = {}
        
        for s in strs:
            # how to sort by char or count
            ascArr = [0 for i in range(58)] 
            for c in s:
                ascArr[ord(c) - 65] += 1
            
            if (map.get(str(ascArr)) is None):
                out.append([s])
                map[str(ascArr)] = len(out) - 1
            else:
                out[map[str(ascArr)]].append(s)
        return out
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])) 
            
                
        
