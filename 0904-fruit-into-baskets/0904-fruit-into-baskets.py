class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        left= 0
        right =0
        max_len = 0
        freq = {}


        for right  in range(n):
            fruit = fruits[right]
            freq[fruit]=freq.get(fruit,0)+1

            #shrink window if more than 2 fruits types
            while len(freq)>2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]] 
                left +=1

            max_len = max(max_len , right-left+1)
        return max_len    


