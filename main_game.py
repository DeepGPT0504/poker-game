import random as rd
from system import *
from action import *

separator = ['-'* 15]

def betting_order(round_num, player_class_order):
    if round_num == 1:
        return player_class_order
    elif round_num == 2:
        return player_class_order[1:] + player_class_order[:1]
    elif round_num == 3:
        return player_class_order[2:] + player_class_order[:2]
    elif round_num == 4:
        return player_class_order[3:] + player_class_order[:3]
    else:
        return player_class_order
    

def main():
    order_1 = 0
    money = 5000
    user_deck = []
    com1_deck = []
    com2_deck = []
    com3_deck = []
    community_card = []
    user = player_action('player', money, user_deck,False,False,False)
    com1 = computer_action('com1', money, com1_deck,False,False,False)
    com2 = computer_action('com2', money, com2_deck,False,False,False)
    com3 = computer_action('com3', money, com3_deck,False,False,False)
    player_order = ['player', 'com1', 'com2', 'com3', 'player']
    player_class_order = [user, com1, com2, com3]
    
    
    while True:
        
        order = order_1 % 4
        ask = input(f'당신의 현재 잔액: {user.money},게임을 진행하시겠습니까?(Y/N):').lower()
        
        if ask == 'n':
            break
       
        else: 
            
            #메인 덱 만들기
            ranks = "23456789TJQKA"
            suits = ["Spade", "Hearts", "Diamonds", "Cloba"]
            deck = [(rank, suit) for rank in ranks for suit in suits] 
            bank = 0
            
            #카드 섞어서 배부
            for i in [user_deck,com1_deck,com2_deck,com3_deck]*2:
                a = rd.randint(0,len(deck)-1)
                i.append(deck[a])
                del deck[a]
           
           #프리 플랍 라운드 시작
            print('Pre-Flop')
            print(f'당신의 손패 입니다: {user_deck}\n')
            print(f'Small blind:{player_order[order]},Big Blind:{player_order[order+1]}')
            player_class_order[order].money -= 250
            player_class_order[order+1].money -= 500
            bank += 750
            current_max_bet = 500

            # 올바른 베팅 순서 적용 (SB 다음 플레이어부터)
            preflop_order = player_class_order[order+2:] + player_class_order[:order+2]
            z_scores = [get_z(p.deck, community_card) for p in preflop_order]
            current_max_bet = round_betting(current_max_bet, preflop_order, z_scores,user, bank)
            bank += current_max_bet * sum(not p.say_fold for p in preflop_order)

            for _ in range(3):
                a = rd.randint(0,len(deck)-1)
                community_card.append(deck[a])
                del deck[a]
            
            for round_num in range(2, 5):
                print(f'\nround {round_num}')

                if round_num <= 3:
                    a = rd.randint(0,len(deck)-1)
                    community_card.append(deck[a])
                    del deck[a]

                print(f'당신의 손패 입니다: {user_deck}')
                print('커뮤니티 카드입니다:', end="")
                show_community_card(round_num - 1, community_card)
                print(f'\n당신의 카드로 해당하는 족보:{determine_jokbo(user_deck,community_card)}')
#오류
#round배팅함수에 플레이어스라는 변수가 배팅순서인데, 이를 적용해서 해결해야함.
                this_round_players = betting_order(round_num, player_class_order)
                z_scores = [get_z(p.deck, community_card) for p in this_round_players]
                
                current_max_bet = round_betting(0, this_round_players, z_scores, user, bank)
                bank += current_max_bet * sum(not p.say_fold for p in this_round_players)

            player_jokbo_dic = {}
            for i in player_class_order:
                if not i.say_fold:
                    player_jokbo_dic[i.player_name] = get_z(i.deck, community_card)

            max_key = max(player_jokbo_dic, key=player_jokbo_dic.get)
            print(player_jokbo_dic)
            if max_key == 'player':
                print(f'승리! {bank}만큼 따셨습니다!')    
                user.money += bank
            else:
                print(f'{max_key} 님의 승리!')
                for p in player_class_order:
                    if p.player_name == max_key:
                        p.money += bank
                        break

            order_1 = order_1 + 1 

            #초기화
            for i in player_class_order:
                i.say_fold = False
                i.say_call = False
                i.say_raise = False

            user_deck = []
            com1_deck = []
            com2_deck = []
            com3_deck = []
            community_card = []

main()

#test