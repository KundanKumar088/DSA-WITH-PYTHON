class Solution(object):
   def minWindow(self, s, t):
       """
       :type s: str
       :type t: str
       :rtype: str
       """
       target = [0] * 256  # Frequency of characters in t
       for ch in t:
           target[ord(ch)] += 1


       n = len(s)
       i = 0
       j = 0
       count = 0
       required = len(t)
       start = 0
       min_len = float('inf')


       while j < n:
           if target[ord(s[j])] > 0:
               count += 1
           target[ord(s[j])] -= 1


           while count == required:
               if min_len > j - i + 1:
                   min_len = j - i + 1
                   start = i


               target[ord(s[i])] += 1
               if target[ord(s[i])] > 0:
                   count -= 1
               i += 1


           j += 1


       return "" if min_len == float('inf') else s[start:start + min_len]
 



        