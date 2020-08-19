# Friday: Creating Blackjack

# importing necessary functions

from random import randint
import os

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

# create the blackjack class, which will hold all game methods and attributes

class Blackjack():
    def __init__(self):
        self.deck = []
        self.suits = ("Spades", "Hearts", "Diamonds", "Clubs")
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

    # create a method that creates a deck of 52 cards, each card 
    # should be a tuple with a value and suit

    def make_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))

    def pull_card(self):
        return self.deck.pop(randint(0,len(self.deck)-1))

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self, dealer_start = True):
        print(f"\n{self.name}")
        print("========")
        for i in range(len(self.hand)):
            if self.name == "Dealer" and i == 0 and dealer_start:
                print("- of -")
            else:
                card = self.hand[i]
                print(f"{card[0]} of {card[1]}")
            print(f"Total = {self.calculate_hand(dealer_start)}")

    def calculate_hand(self, dealer_start = True):
        total = 0
        aces = 0
        card_values = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10, "A":11}

        if self.name == "Dealer" and dealer_start:
            card = self.hand[1]
            return card_values[card[0]]
        for card in self.hand:
            if card[0] == "A":
                aces +=1
            else: 
                total += card_values[card[0]]
        for i in range(aces):
            if total + 11 > 21:
                total += 1
            else: 
                total += 11
        return total
                
def main():
    game = Blackjack()
    game.make_deck()
    player = Player("Alex")
    dealer = Player("Dealer")
    player_bust = False
    while input("Would like to stay of hit?: ").lower() != "s":
        screen_clear()
        player.add_card(game.pull_card())
        player.show_hand()
        dealer.show_hand()
        if player.calculate_hand()>21:
            player_bust = True
            print("You lose!")
            break
        dealer_bust = False
        
        if not player_bust:
            while dealer.calculate_hand(False) < 17:
                dealer.add_card(game.pull_card())
                if dealer.calculate_hand(False) > 21:
                    dealer_bust = True
                    print("You win!")
                    break
        screen_clear()
        player.show_hand()
        dealer.show_hand(False)

    if player_bust:
        print("You busted, better luck next time")
    elif dealer_bust:
        print("The dealer busted, you win!")
    elif dealer.calculate_hand(False) > player.calculate_hand():
        print("Dealer has higher cards, you lose!")
    elif dealer.calculate_hand(False) < player.calculate_hand():
        print("You beat the dealer! Congrats!")
    else:
        print("You pushed, no one wins!")
        
main()