class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        # starting index
        longest_so_far = 1
        chars_in_substring = []
        prev_char = None
        hash_map = {}
        exit_condition = False
        start_index = 0
        current_index = 0
        while not exit_condition:
            for char in s[start_index:]:
                if (char != prev_char) and (char not in chars_in_substring):
                    chars_in_substring.append(char)
                    prev_char = char
                    hash_map[char] = current_index
                else:
                    if len(chars_in_substring) > longest_so_far:   
                        longest_so_far = len(chars_in_substring)
                    chars_in_substring = []
                    start_index = hash_map[char] + 1
                    # char = s[hash_map[char] + 1]
                    # chars_in_substring.append(char)
                    prev_char = None
                    hash_map = {}
                    # start_index = hash_map[char] + 1
                    continue
                current_index += 1
                if len(chars_in_substring) > longest_so_far:   
                    longest_so_far = len(chars_in_substring)
            exit_condition = True
        return longest_so_far