#  Game class

import pygwidgets
import pygame
import random

from Constants import *


# Card Class
class Card:

    def __init__(self, window, rank, suit, value):
        # must add code here to save away parameters in instance variables
        # and create two Image objects, one for the current card, one for the backOfCard
        # you can remove this line when you add your own
        self.window = window
        self.rank = rank
        self.CardName = suit
        self.value = value
        self.image = pygwidgets.Image(window, (0, 0), 'images/' + self.rank + ' of ' + self.CardName + '.png')
        self.backOfImage = pygwidgets.Image(window, (0, 0), 'images/BackOfCard.png')
        self.cardImage = self.image
        self.loc = ''

    def conceal(self):
        self.image = self.backOfImage

    def setLoc(self, locTuple):
        self.image.setLoc(locTuple)
        self.loc = locTuple

    def reveal(self):
        self.image = self.cardImage

    def getName(self):
        return self.CardName

    def getValue(self):
        return self.value

    def draw(self):
        self.image.setLoc(self.loc)
        self.image.draw()

    @staticmethod
    def getCardNameAndValue():
        return ("CardName", 0)


# Deck Class
class Deck:
    SUIT_TUPLE = SUIT_TUPLE_VALUE
    RANK_TUPLE = RANK_TUPLE_VALUE
    STANDARD_VALUES_TUPLE = STANDARD_VALUES_TUPLE_VALUE

    def __init__(self, window, valuesTuple=STANDARD_VALUES_TUPLE):
        # If nothing is passed in for valuesTuple, it uses default values
        self.startingDeckList = []
        self.playingDeckList = []
        for suit in Deck.SUIT_TUPLE:
            for index, rank in enumerate(Deck.RANK_TUPLE):
                oCard = Card(window, rank, suit, valuesTuple[index])
                self.startingDeckList.append(oCard)

    def shuffle(self):
        # make a copy of the starting deck and save in the playing deck list
        self.playingDeckList = self.startingDeckList[:]
        for oCard in self.playingDeckList:
            oCard.conceal()
        random.shuffle(self.playingDeckList)

    def getCard(self):
        if len(self.playingDeckList) == 0:
            raise Exception('No more cards')
        oCard = self.playingDeckList.pop()  # pop one off the deck and return it
        return oCard


# Game Class
class Game:
    CARD_OFFSET = GAME_CARD_OFFSET_VALUE
    CARDS_TOP = GAME_CARDS_TOP_VALUE
    CARDS_LEFT = GAME_CARDS_LEFT_VALUE
    NCARDS = GAME_NCARDS_VALUE

    def __init__(self, window):
        self.window = window
        self.oDeck = Deck(self.window)
        self.score = 100
        self.scoreText = pygwidgets.DisplayText(window, (450, 164), 'Score: ' + str(self.score), fontSize=36, textColor=WHITE, justified='right')
        self.messageText = pygwidgets.DisplayText(window, (50, 460), '', width=900, justified='center', fontSize=36, textColor=WHITE)
        self.loserSound = pygame.mixer.Sound("sounds/loser.wav")
        self.winnerSound = pygame.mixer.Sound("sounds/ding.wav")
        self.cardShuffleSound = pygame.mixer.Sound("sounds/cardShuffle.wav")

        self.cardXPositionsList = []
        thisLeft = Game.CARDS_LEFT
        # Calculate the x positions of all cards ... once
        for i in range(Game.NCARDS):
            self.cardXPositionsList.append(thisLeft)
            thisLeft = thisLeft + Game.CARD_OFFSET
        self.reset()  # start a round of the game

    def reset(self):  # This method is called when a new round starts
        self.score = 100
        self.scoreText.setValue('Score: ' + str(self.score))
        self.cardShuffleSound.play()
        self.cardList = []
        self.oDeck.shuffle()
        for cardIndex in range(0, Game.NCARDS):  # Deal out cards
            oCard = self.oDeck.getCard()
            self.cardList.append(oCard)
            thisXPosition = self.cardXPositionsList[cardIndex]
            oCard.setLoc((thisXPosition, Game.CARDS_TOP))

        self.showCard(0)
        self.cardNumber = 0
        self.currentCardName, self.currentCardValue = self.getCardNameAndValue(self.cardNumber)
        self.messageText.setValue(
            'Starting card is ' + self.currentCardName + '. Will the next card be higher or lower?')

    def getCardNameAndValue(self, index):
        oCard = self.cardList[index]
        theName = oCard.getName()
        theValue = oCard.getValue()
        return theName, theValue

    def showCard(self, index):
        oCard = self.cardList[index]
        oCard.reveal()

    def hitHigherOrLower(self, higherOrLower):
        self.cardNumber = self.cardNumber + 1
        self.showCard(self.cardNumber)
        nextCardName, nextCardValue = self.getCardNameAndValue(self.cardNumber)

        if higherOrLower == HIGHER:
            if nextCardValue > self.currentCardValue:
                self.score = self.score + 15
                self.messageText.setValue('Yes, the ' + nextCardName + ' was higher')
                self.winnerSound.play()
            else:
                self.score = self.score - 10
                self.messageText.setValue('No, the ' + nextCardName + ' was lower')
                self.loserSound.play()

        else:  # user hit the lower button:
            if nextCardValue < self.currentCardValue:
                self.score = self.score + 15
                self.messageText.setValue('Yes, the ' + nextCardName + ' was lower')
                self.winnerSound.play()
            else:
                self.score = self.score - 10
                self.messageText.setValue('No, the ' + nextCardName + ' was higher')
                self.loserSound.play()

        self.scoreText.setValue('Score: ' + str(self.score))
        self.currentCardValue = nextCardValue  # set up for next higher/lower button choice

        done = (self.cardNumber == (Game.NCARDS - 1))  # did we reach the last card?
        return done

    def draw(self):
        # Tell each card to draw itself
        for oCard in self.cardList:
            oCard.draw()

        self.scoreText.draw()
        self.messageText.draw()
