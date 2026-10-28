class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:



        words = set(wordList)

        if endWord not in words:
            return []

        # Distance from beginWord and all shortest-path parents
        dist = {beginWord: 0}
        parents = defaultdict(list)
        queue = deque([beginWord])
        L = len(beginWord)

        while queue:
            word = queue.popleft()
            next_dist = dist[word] + 1

            for i in range(L):
                for ch in ascii_lowercase:
                    if ch == word[i]:
                        continue

                    neighbor = word[:i] + ch + word[i + 1:]

                    if neighbor not in words:
                        continue

                    if neighbor not in dist:
                        dist[neighbor] = next_dist
                        queue.append(neighbor)

                    # Keep every parent at the shortest distance
                    if dist[neighbor] == next_dist:
                        parents[neighbor].append(word)

        if endWord not in dist:
            return []

        # Reconstruct all shortest paths backward
        result = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()

        backtrack(endWord)
        return result
        