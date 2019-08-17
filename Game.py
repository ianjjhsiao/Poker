import Card
import random
import Player

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]


class Game:
    def __init__(self, startingBalance):
        self.startingBalance = startingBalance
        self.deck = list()
        self.players = list()
        self.button = 0;
        self.board = list()
        Game.addCards(self)
        Game.shuffleCards(self)

    def deal(self):
        # burn one at the start
        self.deck.pop()
        # deal two to each player
        start = self.button
        for x in range(2):
            for i in range(len(self.players)):
                if start >= len(self.players):
                    start -= len(self.players)
                self.players[start].hand.append(self.deck.pop())
                start += 1
        self.button += 1
        if self.button >= len(self.players):
            self.button = 0
        # burn one before the flop
        self.deck.pop()
        for x in range(3):
            self.board.append(self.deck.pop())
        # burn one before the turn
        self.deck.pop()
        self.board.append(self.deck.pop())
        # burn one before the river
        self.board.append(self.deck.pop())

    def addPlayer(self, name):
        if len(self.players) < 22:
            self.players.append(Player.Player(name, self.startingBalance))
        else:
            print("Max number of players reached : 22")

    def shufflePlayers(self):
        Game.shuffle(self.players)
        i = 0;
        for p in self.players:
            p.seatOrder = i
            i += 1

    def addCards(self):
        for suit in suits:
            for x in range(13):
                self.deck.append(Card.Card(x, suit))

    def shuffleCards(self):
        Game.shuffle(self,self.deck)

    def shuffle(self,list):
        i = 0
        for c in list:
            rand = random.randint(0, len(list) - 1)
            temp = c
            list[i] = list[rand]
            list[rand] = temp
            i += 1
