class Solution:
    def numOfStrings(self, patterns: list, word: str) -> int:
        cnt = 0
        for p in patterns:
            if p in word:
                cnt += 1
        return cnt


s = Solution()
print(s.numOfStrings(patterns=["a", "abc", "bc", "d"], word="abc") == 3)
print(s.numOfStrings(patterns=["a", "b", "c"], word="aaaaabbbbb") == 2)
print(s.numOfStrings(patterns=["a", "a", "a"], word="ab") == 3)
