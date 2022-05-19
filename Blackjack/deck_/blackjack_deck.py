"""Builds a deck of cards from a list of cards."""

import random

class Card:
    """Defines the individual cards_per_deck."""
    def __init__(self, value, suit, card_value):
        self.value = value
        self.suit = suit
        self.card_value = card_value

    def show(self):
        """Prints the individual cards_per_deck."""
        (f"The {self.value} of {self.suit}'s")

    def card_counter(self, card_value):
        """Returns the value of the card in Blackjack."""
        card_values = {'Ace-Lo': 1, 'Deuce': 2, 'Three': 3, 'Four': 4, 'Five': 5,
                       'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                       'Jack': 10, 'Queen': 10, 'King': 10, 'Ace-High': 11}
        

class Deck:
    """Blackjack deck object."""
    def __init__(self):
        self.cards = []
        self.build_cards()

    def build_cards(self):
        """Iterates a deck of cards"""
        for suit in list('Clubs', 'Diamonds', 'Hearts', 'Spades'):
            for card in list('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'):
                self.cards.append(Card(suit, card))

    def show(self):
        """Prints the deck of cards."""
        for card in self.cards:
            card.show()

    def shuffle(self):
        """Shuffles the deck of cards"""
        for i in range(len(self.cards) -1, 0, 1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw_card(self):
        """Draws the card from cards list."""
        return self.cards.pop()

    def draw(self, deck):
        """Adds the card to the hand."""
        self.hand.append(deck.draw_card())
        return Player.self.hand



class Player:
    """A player class"""
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        """Adds the card to the hand."""
        self.hand.append(deck.draw_card())
        return self

    def show(self):
        """Prints the players hand."""
        for card in self.hand:
            card.show()

