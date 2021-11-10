# https://leetcode.com/problems/next-greater-numerically-balanced-number/discuss/1548038/Python-Simple-Brute-Force-solution


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def count(n):  # 어떤 요소로 몇개 이루어져 있는지 셈
            cnt = [0] * 10
            while n:
                cnt[n % 10] += 1
                n //= 10
            return cnt

        def valid(cnt):
            for i, c in enumerate(cnt):
                if c > 0 and c != i:  # 숫자와 개수가 같으면
                    return False
            return True

        x = n + 1
        while True:
            cnt = count(x)
            if valid(cnt):
                return x
            x += 1


s = Solution()
print(s.nextBeautifulNumber(n=3000))
