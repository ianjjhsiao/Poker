from PIL import Image


class Card:
    names = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        if 0 < number < 10:
            try:
                self.image = Image.open("Card_Images/" + str(number + 1) + suit[0] + ".png")
            except IOError:
                pass
        else:
            try:
                self.image = Image.open("Card_Images/" + str(Card.names[number][0]) + suit[0] + ".png")
            except IOError:
                pass

    def __str__(self):
        # self.image.show()
        return Card.names[self.number] + " Of " + self.suit
