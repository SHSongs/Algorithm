class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        a = (1 << p) - 1

        b = a//2
        print(b)

        ans = (pow(a-1, b, 10**9+7) * a) % 10**9+7

        print(bin(a - 1))

        print(ans)
        return ans


s = Solution()
print(s.minNonZeroProduct(4))

# 581202553
