# TC: O(N)
# SC: O(1)

class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt = 0
        s = list(s)
        print(s)
        i = 0
        length = len(s)

        while i < length:
            if s[i] == 'X':
                i += 3
                cnt += 1
            else:
                i += 1
        return cnt


s = Solution()
print(s.minimumMoves(s="OXOX"))
