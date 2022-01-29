import cards



player_cards=[]
dealer_cards=[]

def print_table():
    print("**********")
    for card in dealer_cards:
        cards.print_card(card)
    print("\n")
    for card in player_cards:
        cards.print_card(card)
    print("**********")

def deal():
    all_card = cards.generate_decks(1)
    player_cards.append(all_card[0])
    player_cards.append(all_card[1])
    
    dealer_cards.append(all_card[2])
    print_table()
    #play
    # dealer_cards.append(all_card[3])
    # print_table()
def reset_cards():
    player_cards.clear()
    dealer_cards.clear()

while(input()==''):
    deal()
    reset_cards()