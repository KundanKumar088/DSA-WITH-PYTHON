class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left , right = 0,0
        charSet =set()
        maxLength = 0

        while right < len(s):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength , right-left+1)
                right +=1
            else:
                charSet.remove(s[left])
                left +=1


        return maxLength        