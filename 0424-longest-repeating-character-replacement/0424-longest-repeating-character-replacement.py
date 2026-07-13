class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        high = 0 
        low= 0
        freq=0
        count={}
        max_length = 0

        for high in range (n):
            count[s[high]]=count.get(s[high],0) +1
            freq =max(freq ,count[s[high]])

            while (high-low+1)-freq >k:
                count[s[low]] -=1
                low +=1

            max_length = max(max_length, high - low + 1)        
        return max_length