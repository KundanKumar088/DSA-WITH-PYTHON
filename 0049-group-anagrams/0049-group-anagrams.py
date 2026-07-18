class Solution(object):
   def getHash(self, s):
       """
       :type s: str
       :rtype: str
       """
       freq = [0] * 26
       for ch in s:
           freq[ord(ch) - ord('a')] += 1


       hash_str = ""
       for i in range(26):
           if freq[i] != 0:
               hash_str += str(freq[i])
           hash_str += "$"
       return hash_str


   def groupAnagrams(self, strs):
       """
       :type strs: List[str]
       :rtype: List[List[str]]
       """
       from collections import defaultdict
       res = []
       mp = defaultdict(list)


       for i in range(len(strs)):
           key = self.getHash(strs[i])
           mp[key].append(strs[i])


       for group in mp.values():
           res.append(group)


       return res




