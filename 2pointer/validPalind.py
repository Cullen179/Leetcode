class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1
        c = ""
        d = ""

        if (b == 0 or b == -1):
            return True
        
        while (a <= b):
            if (not s[a].isalnum()): 
                a += 1
                continue
            if (not s[b].isalnum()):
                b = b - 1
                continue
            
            c = s[a].lower() 
            d = s[b].lower()
            if (s[a].lower() != s[b].lower()): 
                return False
            a += 1
            b = b - 1

        return True

print(Solution.isPalindrome("", "Was it a car or a cat I saw?"))


            
