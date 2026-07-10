class Solution:
    def isPalindrome(self, s: str) -> bool:
       n = len(s)


       low = 0
       high = n - 1


       while low < high:
           if not s[low].isalnum():
               low += 1
           elif not s[high].isalnum():
               high -= 1
           elif s[low].lower() == s[high].lower():
               low += 1
               high -= 1
           else:
               return False
       return True

        