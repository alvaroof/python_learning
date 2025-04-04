class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        longest_so_far = 0
        start_index = 0
        hash_map = {}

        for current_index, char in enumerate(s):
            if char in hash_map and hash_map[char] >= start_index:
                # Move the start to one position after the last occurrence
                start_index = hash_map[char] + 1
            hash_map[char] = current_index
            longest_so_far = max(longest_so_far, current_index - start_index + 1)

        return longest_so_far
    
if __name__ == "__main__":
    s = "abcabcbb"    
    solution = Solution()
    answer = solution.lengthOfLongestSubstring(s)
    print(answer)