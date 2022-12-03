class Date:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        return sum(Date.days[:self.month - 1]) + self.day - (sum(Date.days[:other.month - 1]) + other.day)


jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)
