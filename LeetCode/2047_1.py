import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        sen = sentence.split()
        r, m = 0, 0
        _digits = re.compile('\d')

        def increment(s):  # ! , . 에 따라 증가 결정
            a, b, c = 0, 0, 0
            a = s.count('!')
            b = s.count(',')
            c = s.count('.')

            if (a + b + c) == 0:
                return 1
            elif (a + b + c) == 1:
                if s[-1] in ['!', ',', '.']:  # ! , . 이 마지막에 있으면
                    return 1
            return 0

        for s in sen:
            if not bool(_digits.search(s)):  # 숫자 있는지 검사
                m = s.count('-')  # -의 개수를 샘
                if m == 1:
                    a = s.index('-')  # -의 위치에 따라 증가 결정
                    if a != 0 and a != len(s) - 1 and s[a + 1].isalpha():
                        r += increment(s)
                elif m == 0:
                    r += increment(s)
        return r
