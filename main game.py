import random as rd
from system import *
from action import *



def main():
        
    money = 5000
    while True:
        ask = input(f'당신의 현재 잔액: {money},게임을 진행하시겠습니까?(Y/N):').lower()
        if ask == 'n':
            break
        else: 
            #setting_1
            ranks = "23456789TJQKA"
            suits = ["Spade", "Hearts", "Diamonds", "Cloba"]
            deck = [(rank, suit) for rank in ranks for suit in suits] 
            bank = 0

            #setting_2
            user_deck = []
            com1_deck = []
            com2_deck = []
            com3_deck = []
            community_card = []
            user = player_action('John', money, user_deck)
            bank = 0

            #player card shuffle
            player_list = [user_deck,com1_deck,com2_deck,com3_deck,user_deck,com1_deck,com2_deck,com3_deck] #2장씩 주어야 하기에 2번 반복해서 for구문 반복시킴
            for i in player_list:
                a = rd.randint(0,len(deck)-1)
                i.append(deck[a])
                del deck[a]

            #playing game

            #round 1
            print('round 1')
            for i in range(0,3):
                a = rd.randint(0,len(deck)-1)
                community_card.append(deck[a])
                del deck[a]

            print(f'당신의 손패 입니다: {user_deck}')
            print()
            print('커뮤니티 카드입니다:',end="")
            show_community_card(1, community_card)
            print()
            print()
            print(f'당신의 카드로 해당하는 족보:{determine_jokbo(user_deck,community_card)}')
            bank = bank + user.betting()

            #round 2
            print('round 2')
            a = rd.randint(0,len(deck)-1)
            community_card.append(deck[a])
            del deck[a]

            print(f'당신의 손패 입니다: {user_deck}')
            print()
            print('커뮤니티 카드입니다:',end="")
            show_community_card(2, community_card)
            print()
            print()
            print(f'당신의 카드로 해당하는 족보:{determine_jokbo(user_deck,community_card)}')
            bank = bank + user.betting()

            #round 3
            print('round 3')
            a = rd.randint(0,len(deck)-1)
            community_card.append(deck[a])
            del deck[a]

            print(f'당신의 손패 입니다: {user_deck}')
            print()
            print('커뮤니티 카드입니다:',end="")
            show_community_card(3, community_card)
            print()
            print()
            print(f'당신의 카드로 해당하는 족보:{determine_jokbo(user_deck,community_card)}')
            bank = bank + user.betting()
            
            #플레이어가 이겨서 판돈 얻음
            print(f'승리! {bank}만큼 따셨습니다!')    
            money = bank + user.back_money()

                

        
main()
            
