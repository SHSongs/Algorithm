import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        lst = sentence.split()

        cnt = 0
        for s in lst:
            if len(s) >= 2:
                if s[0] == "," or s[0] == "." or s[0] == "!":
                    continue

            tmp_s = s[0:-1]
            if tmp_s.count("-") + tmp_s.count(".") + tmp_s.count(",") >= 2 and not s[-1] == ".":
                continue

            if "," in s[0:-1] or "." in s[0:-1]:
                continue

            if not s == "-":
                if s == "!" or s[-1] == "!" or s[-1] == ",":
                    cnt += 1
                    print(s)
                    continue

                if not re.sub(r'[^0-9!]', '', s):
                    cnt += 1
                    print(s)

        return cnt


s = Solution()
# print(s.countValidWords("cat and  dog"))
print(s.countValidWords("!this  1-s b8d!"))
# print(s.countValidWords("alice and  bob are playing stone-game10"))
# print(s.countValidWords("he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."))
# print(s.countValidWords("-"))
# print(s.countValidWords("!"))
# print(s.countValidWords("a-b-c"))
# print(s.countValidWords("a-.b"))
# print(s.countValidWords(",aab"))
# print(s.countValidWords("cn,p "))
# print(s.countValidWords("k7 k3fep de1sr6,c  x.s   3q07 v7w  24qr0h2k ,p32u3s"))
# print(s.countValidWords("m-i!"))
# print(s.countValidWords("q-o  x-p! g-l- q-n  f-o, m-u. m-i! y-k, i-j, d-p! e-t, h-u  j-j- d-z- v-w, r-a  i-h. d-a! z-o, v-l, "))
print(s.countValidWords("y-k,"))
