#제작게임: 텍사스 홀덤 게임
#제작기능: 족보판별, 플레이어와 컴퓨터3명의 총 4명의 게임진행 방식을 구현



import random as rd
#python 내장 모듈인 'random'을 불러옴.
from system import *
#같은 파일에 포함된 python파일인 system.py에서 모든 함수/클래스를 불러옴.
from action import *
#위와 같이 action.py에서 모든 함수/클래스를 불러옴.

def main():
#게임전체를 실행하는 함수. 순서, 배팅, 각 참여자의 덱을 설정하는 함수.
    money = 20000
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
    player_order = ['player', 'com1', 'com2', 'com3']
    player_class_order = [user, com1, com2, com3]
    game_end = False #True가 되면 게임 종료
    
#포커 게임의 진행과정을 구성하는 코드    

    print("|===========================================================|")
    ask = input(f'|당신의 현재 잔액: {user.money},게임을 진행하시겠습니까?(Y/N/): ').lower() 
    #게임 진행 여부를 묻는 ask변수
    
    if ask == 'y':
        
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
        print('|라운드가 시작합니다! ::               Pre-Flop             |')
        print(f'|순서는 {player_order}순서로 진행됩니다!|')
        print("+===========================================================+")
        print(f'|당신의 손패 입니다: {user_deck}\n') #현재 나의 카드(user)를 공개개
        print(f'Small blind:{player_order[0]},Big Blind:{player_order[1]}')
        #첫 라운드에 배팅해야하는 최소한의 금액: Small blind, S.b보다 큰 금액...B.b 
        player_class_order[0].money -= 250
        player_class_order[1].money -= 500
        current_max_bet = 500
        #첫 라운드의 user이외의 첫배팅 금액고정..배팅시작준비yy
        #y완료를 의미


        # 올바른 베팅 순서 적용 (SB 다음 플레이어부터)
        preflop_order = player_class_order[2:] + player_class_order[:2]
        z_scores = [get_z(p.deck, community_card) for p in preflop_order]
        current_max_bet = round_betting(current_max_bet, preflop_order, z_scores,user, bank)
        bank += current_max_bet * sum(not p.say_fold for p in preflop_order)


        if com1.say_fold == True and com2.say_fold == True and com3.say_fold == True:
            print('다른 모든 플레이어가 폴드하였습니다.')
        

        else:
            for _ in range(3):
                a = rd.randint(0,len(deck)-1)
                community_card.append(deck[a])
                del deck[a]
            #for 반복문 : 라운드 반복              
            for round_num in range(2, 5):
                print(f'\nround {round_num}')
                #라운드에 대응해 공유카드 1개 추가
                if round_num <= 3:
                    a = rd.randint(0,len(deck)-1)
                    community_card.append(deck[a])#공유카드중 flop을 뽑아 추가
                    del deck[a] #위와 같이 중복카드 삭제

                print(f'당신의 손패 입니다: {user_deck}')
                print('커뮤니티 카드입니다:', end="")
                show_community_card(round_num - 1, community_card)
                print(f'\n당신의 카드로 해당하는 족보:{determine_jokbo(user_deck,community_card)}')
                
                #action의 z_score 계산 코드(족보순위에 따른 점수계산)
                z_scores = [get_z(p.deck, community_card) for p in player_class_order]
                #폴드하지 않은 사람 수만큼 공용배팅머니 증가
                current_max_bet = round_betting(500, player_class_order, z_scores, user, bank)
                bank += current_max_bet * sum(not p.say_fold for p in player_class_order)

                if com1.say_fold == True and com2.say_fold == True and com3.say_fold == True:
                    break

            #라운드별 최종 승자 판별 코드(폴드를 하지않은 이들에 대해 점수 계산)
            player_jokbo_dic_1 = {}
            player_jokbo_dic_2 = {}
            for i in player_class_order:
                if not i.say_fold:
                    player_jokbo_dic_1[i.player_name] = get_z(i.deck, community_card)
                    player_jokbo_dic_2[i.player_name] = determine_jokbo(i.deck,community_card)

            max_key = max(player_jokbo_dic_1, key=player_jokbo_dic_1.get)
            print(player_jokbo_dic_2)
            

            #최종 승자 print
            if max_key == 'player':
                print("+=====================================+")
                print(f'|승리! {bank}만큼 따셨습니다!          |')    
                print("+=====================================+")
                user.money += bank


            else:
                print("+=====================================+")
                print(f'|            {max_key} 님의 승리!           |')
                print("+=====================================+")
                for p in player_class_order:
                    if p.player_name == max_key:
                        p.money += bank
    
    elif ask == 'n':
        print('게임을 종료합니다')
    else:
        print('다시 입력해주세요')
        main()

main()

