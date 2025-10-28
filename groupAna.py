from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            arr = [0] * 26
            for c in s:
                # print(arr[ord(c) - 97])
                arr[ord(c) - 97] += 1
            print(arr)
            arr = [str(a) for a in arr]

            key = '-'.join(arr)
            # ana[key] = ana[+ 1
            # print(ana[key])
            # print(ana.keys)
            if key not in ana:
                ana[key] = [s]
            else:
                val = ana[key]
                ana[key] = val + [s]

            print(ana)

        return ana.values()
    
print(Solution.groupAnagrams(0, ["bdddddddddd","bbbbbbbbbbc"])) 