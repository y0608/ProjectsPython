from cgitb import reset
from counting import cards_value
import cards

NUMBER_DECKS = 1

all_cards = cards.generate_decks(NUMBER_DECKS)
player_cards = []
dealer_cards = []

played_cards = 0


def reset_table_cards():
    player_cards.clear()
    dealer_cards.clear()


def reset_game():
    global played_cards
    all_cards = cards.generate_decks(NUMBER_DECKS)
    played_cards = 0
    reset_table_cards()


def print_table():
    print("**********")
    for card in dealer_cards:
        cards.print_card(card)
    print(cards_value(dealer_cards))
    print("\n")
    for card in player_cards:
        cards.print_card(card)
    print(cards_value(player_cards))
    print("**********")


def give_player_card():
    player_cards.append(all_cards[-1])
    all_cards.pop()


def give_dealer_card():
    dealer_cards.append(all_cards[-1])
    all_cards.pop()


def deal():
    global played_cards
    give_player_card()
    give_player_card()
    give_dealer_card()
    played_cards += 3


def game():  
    while(len(all_cards) != 0):
        deal()
        print_table()
        # player_play()
        # dealer_play() #dealer stand on 17?!
        reset_table_cards()
        
game()


# def trainer():
#     while(len(all_cards) != 0):
#         deal()
        
#         reset_table_cards()
# TODO: gamemodes
    #you vs dealer
    #you and other bots on the table vs dealer
    #bot vs dealer
    #basic strategy trainer
        #only soft,hard or splitting
    #card counting trainer
    
# TODO: ui
