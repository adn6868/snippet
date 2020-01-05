class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        current = [price, 1]
        if len(self.stack) == 0:
            self.stack.append(current)
            return current[1]

        i = -1
        peak = self.stack[i]
        while peak[0] <= current[0]:
            # print(peak)
            # print(current)
            # if current[0] == 70:
            #     print('peak = ', peak)
            #     print('current= ',current)
            # peak = self.stack[i]
            current[1] += peak[1]
            i = i - peak[1]
            try:
                peak = self.stack[i]
            except:
                break

        self.stack.append(current)
        return current[1]


def main():
    SS = StockSpanner()
    alist = [31, 41, 48, 59, 79]
    alist2 = [100, 80, 60, 70, 60, 75, 85]
    alist3 = [28, 14, 28, 35, 46, 53, 66, 80, 87, 88]
    for i in alist3:
        print(SS.next(i))


main()
