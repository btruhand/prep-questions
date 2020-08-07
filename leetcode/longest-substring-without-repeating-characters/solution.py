class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        res = 0
        beginning = 0
        for idx, c in enumerate(s):
            length = idx - beginning  # substring length
            res = length if length > res else res
            # if character in hash, and character index is after within the current considered substring
            if c in hash and beginning <= hash[c]:
                # new beginning, 1 over the index of the first time the duplicated
                # character is seen -> because if starting from the index of current character then it would
                # immediately be a duplicate
                # (substring of the substring found is already subsumed by current substring, so no need to care)
                beginning = hash[c] + 1
            hash[c] = idx  # store new beginning of character

        # final calculation in case longest substring reaches the end
        length = len(s) - beginning  # substring length
        res = length if length > res else res

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("a") == 1)
    print(solution.lengthOfLongestSubstring("") == 0)
    print(solution.lengthOfLongestSubstring("aaaaaaa") == 1)
    print(solution.lengthOfLongestSubstring("abcabcbb") == 3)
    print(solution.lengthOfLongestSubstring("pwwkew") == 3)
    print(solution.lengthOfLongestSubstring("dvdf") == 3)
    print(solution.lengthOfLongestSubstring("abecba") == 4)
