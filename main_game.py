import random as rd
#python 내장 모듈인 'random'을 불러옴.
from system import *
#같은 파일에 포함된 python파일인 system.py에서 모든 함수/클래스를 불러옴.
from action import *
#위와 같이 action.py에서 모든 함수/클래스를 불러옴.


def betting_order(round_num, player_class_order):
#round_num : 현재 게임의 라운드 번호를 지정하는 변수. 라운드별 게임은 순차적으로 1칸씩 밀림.
#player_class_order : 진행중인 게임의 플레이어 객체들이 정해진 순서대로 들어있는 리스트를 제작하는 변수.
#총 4개의 라운드로 진행되며, 1,2,3,4 라운드일때마다의 플레이 순서를 명시한 코드    
    if round_num == 1:
        return player_class_order
#라운드1 첫 리스트 그대로 게임 진행.
    elif round_num == 2:
        return player_class_order[1:] + player_class_order[:1]
#라운드2 첫 리스트에서 첫순서인 user를 맨 뒤로 보내는 과정. 밑 과정은 이 과정을 반복.
#[:1],[1:]은 1칸 왼쪽으로 이동시킴.(2,3이면 2칸, 3칸이 이동함)
    elif round_num == 3:
        return player_class_order[2:] + player_class_order[:2]
# 위와 동일
    elif round_num == 4:
        return player_class_order[3:] + player_class_order[:3]
# 위와 동일
    else:
        return player_class_order
# 위와 동일(라운드 4에서 게임은 끝나지만, 라운드가 5이상 넘어간다면 처음으로 돌아가는데 사용됨.)

def main():
#게임전체를 실행하는 함수. 순서, 배팅, 각 참여자의 덱을 설정하는 함수.
    order_1 = 0
    #턴 순서 초기화.
    money = 5000
    #user, com1, com2, com3의 초기 보유 금액 배정(초기화).
    user_deck = []
    com1_deck = []
    com2_deck = []
    com3_deck = []
    community_card = []
    #참여자 4명과 공유카드(community_card)의 덱 리스트(초기화상태로 시작)
    #참여자는 각각 2장의 카드, 공유카드는 총 5개 배정
    user = player_action('player', money, user_deck,False,False,False)
    com1 = computer_action('com1', money, com1_deck,False,False,False)
    com2 = computer_action('com2', money, com2_deck,False,False,False)
    com3 = computer_action('com3', money, com3_deck,False,False,False)
    #4명의 참가자에 대한 정보(이름, 보유금액, 카드덱(리스트), 콜, 폴드, 레이즈) 
    #4명의 참가자 모두 게임 시작시 콜, 폴드, 레이즈를 하지 않기에 False로 초기화한 상태에서 시작
    player_order = ['player', 'com1', 'com2', 'com3', 'player']
    player_class_order = [user, com1, com2, com3]
    
#포커 게임의 진행과정을 구성하는 코드    
    while True: #라운드 종료 시점까지 반복.(True)
        
        order = order_1 % 4 #저장되는 턴 번호로 참가자 플레이 순서를 정하기 위함.
        ask = input(f'당신의 현재 잔액: {user.money},게임을 진행하시겠습니까?(Y/N):').lower()
        #게임 진행 여부를 묻는 ask변수
        if ask == 'n':
            break
       #if함수로 게임진행을 원하지 않을 시 while루프를 빠져나가는 코드
        else: 
        #이외상황은 게임정상 진행.
            
            #메인 덱 만들기
            ranks = "23456789TJQKA"
            suits = ["Spade", "Hearts", "Diamonds", "Cloba"]
            deck = [(rank, suit) for rank in ranks for suit in suits] 
            bank = 0 #공용배팅머니 초기화
            #총 52장을 구성함.(13개(rank) X 4개(suit)) 


            #카드 섞어서 배부
            for i in [user_deck,com1_deck,com2_deck,com3_deck]*2: #카드 덱 배부를 2회 반복.
                a = rd.randint(0,len(deck)-1) #무작위 배정(rd 사용)
                i.append(deck[a]) 
                del deck[a]
                #중복배정방지를 위한 분배덱에서 카드제거.


           #프리 플랍 라운드 시작
            print('Pre-Flop')
            print(f'당신의 손패 입니다: {user_deck}\n') #현재 나의 카드(user)를 공개개
            print(f'Small blind:{player_order[order]},Big Blind:{player_order[order+1]}')
            #첫 라운드에 배팅해야하는 최소한의 금액: Small blind, S.b보다 큰 금액...B.b 
            player_class_order[order].money -= 250
            player_class_order[order+1].money -= 500
            bank += 750
            current_max_bet = 500
            #첫 라운드의 user이외의 첫배팅 금액고정..배팅시작준비완료를 의미

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