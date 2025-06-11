import random as rd
from system import *
from action import *



def main():
    order = 0
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
            user = player_action('player', money, user_deck,False,False,False)
            com1 = computer_action('com1', money, com1_deck,False,False,False)
            com2 = computer_action('com2', money, com2_deck,False,False,False)
            com3 = computer_action('com3', money, com3_deck,False,False,False)
            player_order = ['player','com1','com2','com3','player']
            player_class_order = [user,com1,com2,com3,]
            player_deck_order = [user_deck,com1_deck,com2_deck,com3_deck,user_deck]
            bank = 0

            #player card shuffle
            player_list = [user_deck,com1_deck,com2_deck,com3_deck,user_deck,com1_deck,com2_deck,com3_deck] #2장씩 주어야 하기에 2번 반복해서 for구문 반복시킴
            for i in player_list:
                a = rd.randint(0,len(deck)-1)
                i.append(deck[a])
                del deck[a]

            #playing game

            #round 1
            print('Pre-Flop')
            for i in range(0,3):
                a = rd.randint(0,len(deck)-1)
                community_card.append(deck[a])
                del deck[a]

            print(f'당신의 손패 입니다: {user_deck}')
            print()
            print(f'Small blind:{player_order[order]},Big Blind:{player_order[order+1]}')
            print(f'기본 베팅금:500, {player_order[order]}의 잔액 -250, {player_order[order+1]}의 잔액 -500')
            player_class_order[order].minus_money(250)
            player_class_order[order+1].minus_money(500)
            bank = bank + 750
            current_max_bet = 500
            order = order + 2
            while True:
                if all(p.say_call for p in [user, com1, com2, com3]) == True:
                    break

                current_player = player_class_order[order]

                if current_player.player_name == "player":
                    bet_money = current_player.actions(current_max_bet)
                else:
                    bet_money = current_player.actions(current_max_bet, get_z(player_deck_order[order],community_card))

                if bet_money > current_max_bet:
                    current_max_bet = bet_money 

                if order == 3:
                    order = 0
                else:
                    order += 1
            
            x = 0

            for i in player_class_order:
                if i.say_fold == False:
                    i.minus_money(current_max_bet)
                    x = x + 1
            bank = bank + current_max_bet * x 

            #round 2
            print('round 2')
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
            
            current_max_bet = 0
            while True:
                if all(p.say_call for p in [user, com1, com2, com3]) == True:
                    break

                current_player = player_class_order[order % 4]

                if current_player.name == "player":
                    bet_money = current_player.actions(current_max_bet)
                else:
                    bet_money = current_player.actions(current_max_bet, get_z(player_deck_order[order % 4], community_card))

                if bet_money > current_max_bet:
                    current_max_bet = bet_money 

                order += 1

            for i in player_class_order:
                if i.say_fold == False:
                    i.minus_money(current_max_bet)
                    x = x + 1
            bank = bank + current_max_bet * x 

            #round 3
            print('round 3')
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
            current_max_bet = 0
            while True:
                if all(p.say_call for p in [user, com1, com2, com3]) == True:
                    break

                current_player = player_class_order[order % 4]

                if current_player.name == "player":
                    bet_money = current_player.actions(current_max_bet)
                else:
                    bet_money = current_player.actions(current_max_bet, get_z(player_deck_order[order % 4], community_card))

                if bet_money > current_max_bet:
                    current_max_bet = bet_money 

                order += 1

            for i in player_class_order:
                if i.say_fold == False:
                    i.minus_money(current_max_bet)
                    x = x + 1
            bank = bank + current_max_bet * x 

            #round 4

            print(f'당신의 손패 입니다: {user_deck}')
            print()
            print('커뮤니티 카드입니다:',end="")
            show_community_card(3, community_card)
            print()
            print()
            print(f'당신의 카드로 해당하는 족보:{determine_jokbo(user_deck,community_card)}')
            current_max_bet = 0
            while True:
                if all(p.say_call for p in [user, com1, com2, com3]) == True:
                    break

                current_player = player_class_order[order % 4]

                if current_player.name == "player":
                    bet_money = current_player.actions(current_max_bet)
                else:
                    bet_money = current_player.actions(current_max_bet, get_z(player_deck_order[order % 4], community_card))

                if bet_money > current_max_bet:
                    current_max_bet = bet_money 

                order += 1

            for i in player_class_order:
                if i.say_fold == False:
                    i.minus_money(current_max_bet)
                    x = x + 1
            bank = bank + current_max_bet * x 


            player_jokbo_dic = {}
            for i in player_class_order:
                if i.say_fold == False:
                    player_jokbo_dic[i.name] = get_z(i.deck, community_card)

                max_key = max(player_jokbo_dic, key=player_jokbo_dic.get)
                if max_key == 'player':
                    print(f'승리! {bank}만큼 따셨습니다!')    
                    user.money = user.money + bank
                else:
                    if max_key == 'com1':
                        print('com1 님의 승리!')
                        com1.money = com1.money + bank

                    elif max_key == 'com2':
                        print('com2 님의 승리!')
                        com1.money = com2.money + bank

                    elif max_key == 'com3':
                        print('com3 님의 승리!')
                        com1.money = com3.money + bank
                    
           
main()
            
