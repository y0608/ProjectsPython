# -*- coding: utf-8 -*-
import itertools
import random


vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
deck = list(itertools.product(vals, suits))

def card_value(card):
    if(card[0]>='2' or card[0]<='10'):
        return int(card[0])
    if(card[0]=='J' or card[0]=='Q' or card[0]=='K')
    return 10

def generate_decks(number_of_decks):
    all_decks = []
    for i in range(number_of_decks):
        deck = list(itertools.product(vals, suits))
        random.shuffle(deck)
        all_decks.extend(deck)
    return all_decks


def print_card(card):
    if(card[1] == 'spades'):
        print(card[0]+'♠')
    elif(card[1] == 'clubs'):
        print(card[0]+'♣')
    elif(card[1] == 'hearts'):
        print(card[0]+'♥')
    elif(card[1] == 'diamonds'):
        print(card[0]+'♦')


def print_deck(deck):
    for card in deck:
        print_card(card)

