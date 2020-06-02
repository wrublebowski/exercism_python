suits = ['Kier', 'Karo', 'Pik', 'Trefl']

ranks = ['Dwójka', 'Trójka', 'Czwórka', 'Piątka', 'Szóstka',
         'Siódemka', 'Ósemka', 'Dziewiątka', 'Dziesiątka',
         'Walet', 'Królowa', 'Król', 'As']

values = {'Dwójka': 2, 'Trójka': 3, 'Czwórka': 4, 'Piątka': 5,
          'Szóstka': 6, 'Siódemka': 7, 'Ósemka': 8, 'Dziewiątka': 9,
          'Dziesiątka': 10, 'Walet': 10, 'Królowa': 10, 'Król': 10, 'As': 11}

gra = True

import random
import math

class Card:

    def __init__(self, rank, suit):
        # wartości i nominały
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # do drukowania poleceniem print()
        return str(self.rank + ' ' + self.suit)

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        sprawdzenie_talii = ''
        for card in self.deck:
            sprawdzenie_talii += card.__str__() + '\n'
        return 'W mej talii zawierają się:\n\n' + sprawdzenie_talii

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        # obiekt to będzie card podany w tej metodzie w nawiasie, to będzie obiekt klasy Card
        # card.rank jest z klasy Card
        # odsyła on do wartości, np. 'Walet' - wartość to 10
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            # if 'As' in self.cards:
        #   self.aces+=1
        # else:
        #   pass

class Chips:

    def __init__(self, total=100):
        self.total = total  # a default total value
        # pass in an override value at the time the object was created
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Ile chcesz postawić? '))
        except:
            print('Proszę o kwotę w złotych, bez groszy.')
        else:
            if chips.bet > chips.total:
                print(f'Możesz obstawić maxymalnie do kwoty {chips.total}')
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global gra  # to control an upcoming while loop

    while True:
        dobranie = input('DOBIERAMY KARTY? Tak lub nie: ')

        if dobranie[0].lower() == 't':
            hit(deck, hand)
        elif dobranie[0].lower() == 'n':
            print("No to teraz Dealer gra.\n")
            gra = False
        else:
            print('Sorki, spróbuj jeszcze raz!')
            continue
        break

def show_some(player, dealer):
    print('\nKARTY GRACZA TO:', *player.cards, sep='\n')
    print('KARTY DEALERA TO:\n1 ukryta i', dealer.cards[1], '\n')

def show_all(player, dealer):
    print('\nKARTY GRACZA TO:', *player.cards, sep='\n')
    print('PUNKTY GRACZA:', player.value)
    print('KARTY DEALERA TO:', *dealer.cards, sep='\n')
    print('PUNKTY DEALERA:', dealer.value, '\n')

def player_busts(player, dealer, chips):
    chips.lose_bet()
    print('NASTĘPNYM RAZEM SIĘ UDA! \nTwój aktualny stan konta to:', chips.total)

def player_wins(player, dealer, chips):
    chips.win_bet()
    print('BRAWO! Aktualny stan Twojego konta to:', chips.total)

def dealer_busts(player, dealer, chips):
    print("DEALER BUSTS!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('DEALER WYGRYWA!')
    chips.lose_bet()

def push(player, dealer):
    print('UDAŁO SIĘ, REMIS!!')

while True:

    print('Witam w BlackJack! \nZnajdź się jak najbliżej 21, by wygrać!')

    talia = Deck()
    player1 = Hand()
    dealer1 = Hand()

    talia.shuffle()

    # 2 cards for each player
    player1.add_card(talia.deal())
    player1.add_card(talia.deal())
    dealer1.add_card(talia.deal())
    dealer1.add_card(talia.deal())

    # Set up the Player's chips
    playerbet = Chips(int(input('Ile chcesz mieć w banku? Podaj kwotę: ')))  # with default value 100

    # Prompt the Player for their bet
    take_bet(playerbet)

    # Show cards (but keep one dealer card hidden)
    show_some(player1, dealer1)

    while gra:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(talia, player1)

        # Show cards (but keep one dealer card hidden)
        show_some(player1, dealer1)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player1.value > 21:
            player_busts(player1, dealer1, playerbet)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

    if player1.value <= 21:
        while dealer1.value < 17:
            hit(talia, dealer1)

        # Show all cards
        show_all(player1, dealer1)

        if dealer1.value > 21:
            dealer_busts(player1, dealer1, playerbet)

        elif dealer1.value > player1.value:
            dealer_wins(player1, dealer1, playerbet)

        elif dealer1.value < player1.value:
            player_wins(player1, dealer1, playerbet)

        else:
            push(player1, dealer1)

    # Inform Player of their chips total
    print('PLEJER MA NA KONCIE: ', playerbet.total)

    # Ask to play again
    next_turn = input('Czy chcesz grać dalej? Tak / nie: ')

    if next_turn[0].lower() == 't':
        gra = True
        continue

    else:
        print('Dzięki za rozgrywkę!')
        break