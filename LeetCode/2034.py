
# http://www.grantjenks.com/docs/sortedcontainers/sortedlist.html

# 그냥 list로 하였더니 time out
# list.remove의 TC가 O(N)
# sortlist의 remove의 TC는 O(log(N))

# TC: O(log(N))
# SC: O(update 호출 횟수)

from sortedcontainers import SortedList


class StockPrice:

    def __init__(self):
        self.dict = {}
        self.current_timestamp = -1
        self.sortlist = SortedList([])

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.dict:
            self.sortlist.remove(self.dict[timestamp])

        self.sortlist.add(price)
        self.dict[timestamp] = price
        self.current_timestamp = max(timestamp, self.current_timestamp)

    def current(self) -> int:
        return self.dict[self.current_timestamp]

    def maximum(self) -> int:
        return self.sortlist[-1]

    def minimum(self) -> int:
        return self.sortlist[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

