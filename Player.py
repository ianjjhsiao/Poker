class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = list()
        self.amountInPot = 0
        self.isAllIn = False
        self.hasFolded = False
        self.seatOrder = None

    def check(self):
        pass

    def bet(self, amount):
        self.balance -= amount
        self.amountInPot += amount

    def fold(self):
        self.hasFolded = True

    def allIn(self):
        self.amountInPot += self.balance
        self.balance = 0
        isAllIn = True
