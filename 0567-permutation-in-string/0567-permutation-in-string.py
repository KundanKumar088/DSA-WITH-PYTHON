class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        count1 = [0] *26  
        count2 = [0]*26

        for i in range(n1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1 

        if count1 == count2:
            return True

        j=0
        for i in range(n1,n2):
            count2[ord(s2[i]) - ord('a')] +=1
            count2[ord(s2[j]) - ord('a')] -=1  
            if count1 == count2:
                return True
            j +=1 
        return False         

        