import random

"""
move represents type of move
    f = forward
    b = backward
    l = turn left
    r = turn right
    u = u-turn
"""

class Card:
    def __init__(self, move, amount):
        self.move = move
        self.amount = amount

    #def __repr__(self):
    #    return str(self)

    def __str__(self):
        return str((self.move.upper(), self.amount))

class Deck:
    def shuffleList(self):
        myDeck = []
        f = open('cards.txt', 'r')
        for line in f:
            line = line.replace('\n', '')
            move, amount = line.split(', ')
            newCard = Card(move, amount)
            myDeck.append(newCard)
        random.shuffle(myDeck)
        return myDeck


    def __init__(self):
        self.cardList = self.shuffleList()

    def printDeck(self):
        for card in self.cardList:
            print(card.move.upper(), card.amount)

    def printCard(self):
        cardNum2 = 1
        while cardNum2 != 0:
            return(self.cardList.pop())
            cardNum2 -=1

    #def readCard(self):


class Hand(Deck):
    def __init__(self):
        self.hand = []

    def printHand(self):
        for x in self.hand:
            print(str(x))

    def addToHand(self, card):
        self.hand.append(card)

    def removeFromHand(self, card):
        self.hand.remove(card)





"""
    def printCardStart(self):
        cardNum = 5
        print("this is printed via printCardStart")
        while cardNum != 0:
            print(self.cardList.pop())
            cardNum -=1
"""



d = Deck()
d.shuffleList()
#d.printDeck()
#print(d.printCard())
#d.readCard()


o = Hand()

g = Hand()

if __name__ == "__main__":
    c=Card('f', '1')
    c2=Card('l', '1')
    o.addToHand(c)
    o.addToHand(c2)
    o.printHand()
