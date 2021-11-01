# TC: O(len(s))
# SC: O(1)

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        lst = s.split(' ')

        prev_num = -999
        for i in lst:
            if i.isdigit() is True:
                int_i = int(i)
                if prev_num < int_i:

                    prev_num = int_i
                else:
                    return False
        return True


s = Solution()
print(s.areNumbersAscending(s="1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
print(s.areNumbersAscending(s="hello world 5 x 5"))
print(s.areNumbersAscending(s="sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))
print(s.areNumbersAscending(s="4 5 11 26"))
