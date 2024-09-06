# 1. Find the consecutive days the stock price is less than or equal to the current day
# 2. Store the local maximas in the stack, with the number of consecutive days observed for each local maxima
# 3. If you want the maximum for the current, pop all the elements in the stack which are less than or equal to the current price

class StockSpanner:

    def __init__(self):
        self.stack = deque()

    def next(self, price: int) -> int:
        
        con_days = 1
        while self.stack and price >= self.stack[-1][0]:
            con_days+=self.stack.pop()[1]
        self.stack.append((price,con_days))

        return con_days