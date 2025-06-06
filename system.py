import random as rd

def initial_setting():
    
        #setting
        ranks = "23456789TJQKA"
        suits = ["Spade", "Hearts", "Diamonds", "Cloba"]
        deck = [(rank, suit) for rank in ranks for suit in suits]

        #deck
        user_deck = []
        com1_deck = []
        com2_deck = []
        com3_deck = []
        community_card = []

        #player card shuffle
        player_list = [user_deck,com1_deck,com2_deck,com3_deck,user_deck,com1_deck,com2_deck,com3_deck] #2장씩 주어야 하기에 2번 반복해서 for구문 반복시킴
        for i in player_list:
            a = rd.randint(0,len(deck))
            i.append(deck[a])
            del deck[a]

        #community card shuffle
        for i in range(0,3):
              a = rd.randint(0,len(deck))
              community_card.append(deck[a])
              del deck[a]
