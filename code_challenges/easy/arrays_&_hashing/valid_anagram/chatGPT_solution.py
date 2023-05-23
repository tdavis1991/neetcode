class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base case: Check if the lengths are different
        if len(s) != len(t):
            return False

        char_count = {}

        # Increment count for characters in s
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Decrement count for characters in t
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:
                    del char_count[char]
            else:
                return False

        # If char_count is empty, all characters are accounted for
        return len(char_count) == 0
