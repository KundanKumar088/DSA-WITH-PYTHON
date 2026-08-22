import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)
        heap = []

        class Node:
            def __init__(self, word, count):
                self.word = word
                self.count = count

            def __lt__(self, other):
                if self.count != other.count:
                    return self.count < other.count

                # For same frequency,
                # lexicographically larger word is "smaller"
                return self.word > other.word

        for word, count in freq.items():
            heapq.heappush(heap, Node(word, count))

            if len(heap) > k:
                heapq.heappop(heap)

        result = [node.word for node in heap]

        result.sort(key=lambda word: (-freq[word], word))

        return result  

        