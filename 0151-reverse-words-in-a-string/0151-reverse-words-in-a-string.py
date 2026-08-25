class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        newwords =[]

        for i in range(len(words)):
            newwords.append(words[len(words)-1 - i])

        result= " ".join(newwords)

        return result    