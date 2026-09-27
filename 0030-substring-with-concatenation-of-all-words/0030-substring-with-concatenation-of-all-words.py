class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        required = {}

        for word in words:
            required[word] = required.get(word, 0) + 1

        ans = []

        for offset in range(word_len):
            left = offset
            right = offset
            current = {}
            used = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word not in required:
                    current = {}
                    used = 0
                    left = right
                    continue

                current[word] = current.get(word, 0) + 1
                used += 1

                while current[word] > required[word]:
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    used -= 1

                if used == word_count:
                    ans.append(left)

                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    used -= 1

        return ans
        