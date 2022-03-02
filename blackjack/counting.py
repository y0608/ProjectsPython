

def card_value(card):
    if(card[0]=='2' or card[0]=='3' or card[0]=='4' or card[0]=='5' or card[0]=='6'):
        return 1
    if(card[0]=='7' or card[0]=='8' or card[0]=='9'):
        return 0
    else:
        return -1
#TODO:
#deck estimation -> imam kolko karti sa izigrani prosto trqbva da razdelq na 54?>?
#running count
#true count