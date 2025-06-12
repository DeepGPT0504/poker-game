import random as rd

class player_action(): #player가 사용하는 행동

    def __init__(self, player_name, money, deck, say_fold,say_call,say_raise):
        self.player_name = str(player_name) #플레이어 이름 저장
        self.money = int(money) #플레이어 보유 금액 저장
        self.deck = deck #플레이어가 가지고 있는 덱 저장
        self.say_fold = say_fold #플레이어의 폴드 선언 여부
        self.say_call = say_call #플레이어의 콜 선언 여부
        self.say_raise = say_raise #플레이어의 레이즈 선언 여부

    #플레이어의 행동 모음+a
    def actions(self, bet_money):
        while True:
            if self.say_fold == True:
                print('턴이 넘겨집니다.')
                return bet_money
            else:
                question = input(f'무엇을 하시겠습니까?(레이즈/콜/폴드) \n 현재 베팅 금액:{bet_money}: ')
                
                #레이즈
                if question == '레이즈':
                    while True:

                        question_2 = input(f'얼마를 레이즈하시겠습니까?(현재 판돈{bet_money},현재 잔액{self.money})(취소): ')
                        if type(question_2) == int and bet_money + question_2 > self.money:
                            question_3 = input('잔액이 부족합니다! 올인하시겠습니까?(y/n)').lower()
                            if question_3 == 'y':
                                return self.money
                        elif question_2 == '취소':
                            self.actions(bet_money)
                        else: 
                            self.say_raise = True
                            return bet_money + int(question_2)
                    
                #콜
                elif question == '콜':
                    self.say_call = True
                    return 0
                
                #폴드
                elif question == '폴드':
                    self.say_fold = True
                    return 0
                else:
                    print('다시 입력해주세요')


class computer_action(): #computer_player가 사용하는 행동

    def __init__(self, player_name, money,deck,say_fold,say_call,say_raise):
        self.player_name = player_name
        self.money = money
        self.deck = deck
        self.say_fold = say_fold
        self.say_call = say_call
        self.say_raise = say_raise

    #컴퓨터가 본인 족보에 따라 z점수를 받아서 자신의 기준을 정한다
    def cal_betting_momney(self, z_score): 
        x = rd.randint(0,10)
             
        if z_score <= 30 and x <= 7: #손 패가 원 페어 이하일 때 30% 확률로 컴퓨터가 거짓 베팅을 시도한다
            betting_money = self.money * (rd.randint(20,50)/100)
            return betting_money
            
        elif z_score >= 60 and x <= 6: #손 패가 스트레이트 이상일 때 40% 확률로 거짓 베팅을 시도한다
                betting_money = self.money * (rd.randint(10,30)/100)
                return betting_money
            
        else: #정석 베팅
            if z_score == 100: #현재 보유 금액의 50%부터 80% 사이로 랜덤하게 베팅
                betting_money = self.money * (rd.randint(50,80)/100)
                return int(betting_money)
            
            elif z_score == 90: #현재 보유 금액의 40%부터 60% 사이로 랜덤하게 베팅
                betting_money = self.money * (rd.randint(40,60)/100)
                return int(betting_money)
            
            elif z_score == 80: #현재 보유 금액의 30%부터 50% 사이로 랜덤하게 베팅
                betting_money = self.money * (rd.randint(30,50)/100)
                return int(betting_money)
            
            elif z_score == 70: #현재 보유 금액의 15%부터 50% 사이로 랜덤하게 베팅
                betting_money = self.money * (rd.randint(15,50)/100)
                return int(betting_money)
            
            elif z_score == 60: #현재 보유 금액의 5%부터 45% 사이로 랜덤하게 베팅
                betting_money = self.money * (rd.randint(5,45)/100)
                return int(betting_money)
            
            elif z_score == 50: #현재 보유 금액의 5%부터 30% 사이로 랜덤하게 베팅
                betting_money = self.money * (rd.randint(5,30)/100)
                return int(betting_money)
            
            elif z_score == 40: #현재 보유 금액의 5%부터 30% 사이로 랜덤하게 베팅
                betting_money = self.money * (rd.randint(5,30)/100)
                return int(betting_money)
            
            elif z_score == 30: #현재 보유 금액의 5%부터 30% 사이로 랜덤하게 베팅
                betting_money = self.money * (rd.randint(5,30)/100)
                return int(betting_money)
            
            else: #현재 보유 금액의 5% 부터 20% 사이로 랜덤하게 베팅
                betting_money = self.money * (rd.randint(5,20)/100)
                return int(betting_money)
            
        
    #컴퓨터 플레이어가 하는 행동 모음음
    def actions(self,bet_money,z_score,bank):
        degree = self.cal_betting_momney(z_score)
        while True:
            if self.say_fold == True:
                return bet_money
            else:
                if bank >= degree:
                    self.say_call = True
                    return 0 # 콜
                
                elif z_score >= 70 and bet_money <= degree : #레이즈_1
                    bet_money = bet_money + (self.money / 8)
                    self.say_raise = True
                    return bet_money
                
                elif z_score >= 30 and bet_money <= degree: #레이즈_2
                    bet_money = bet_money + (self.money / 8)
                    self.say_raise = True
                    return bet_money
                
                elif z_score < 30 and bet_money >= 2 * degree: #폴드
                    self.say_fold = True
                    return 0
                
                else:
                    self.say_call = True
                    return 0 # 콜
                

                    



                    




        