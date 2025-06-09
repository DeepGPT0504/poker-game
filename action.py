import random as rd

class player_action(): #player가 사용하는 행동

    def __init__(self, player_name, money, deck, say_fold,say_call):
        self.player_name = str(player_name)
        self.money = int(money)
        self.deck = deck
        self.say_fold = say_fold
        self.say_call = say_call

    def actions(self, bet_money):
        while True:
            if self.say_fold == True:
                print('턴이 넘겨집니다.')
                return bet_money
            else:
                question = input('(레이즈/콜/폴드)?: ')
                if question == '레이즈':
                    question_2 = input(f'얼마를 레이즈하시겠습니까?(현재 판돈{bet_money},현재 잔액{self.money}): ')
                    if bet_money + question_2 > self.money:
                        print('잔액이 부족합니다')
                    else:
                        return bet_money + question_2
                elif question == '콜':
                    self.say_call = True
                    return bet_money
                elif question == '폴드':
                    self.say_fold = True
                    return bet_money
                else:
                    print('다시 입력해주세요')

        
    def back_money(self): #class에 저장된 금액 반환
        return self.money
    
    def minus_money(self, x): #class에 저장된 돈 삭감
        self.money = self.money - x

class computer_action(): #computer_player가 사용하는 행동

    def __init__(self, player_name, money,say_fold,say_call):
        self.player_name = player_name
        self.money = money
        self.say_fold = say_fold
        self.say_call = say_call

    def cal_betting_momney(self, z_score):
        x = rd.randint(0,10)

        if z_score <= 30 and x <= 7: #손 패가 원 페어 이하일 때 30% 확률로 컴퓨터가 거짓 베팅을 시도한다
            betting_money = self.money * (rd.randint(40,80)/100)
            return betting_money
        elif z_score >= 60 and x <= 6: #손 패가 스트레이트 이상일 때 40% 확률로 거짓 베팅을 시도한다
            betting_money = self.money * (rd.randint(10,40)/100)
            return betting_money
        else: #정석 베팅
            if z_score == 100:
                betting_money = self.money * (rd.randint(70,100)/100)
                return betting_money
            elif z_score == 90:
                betting_money = self.money * (rd.randint(60,80)/100)
                return betting_money
            elif z_score == 80:
                betting_money = self.money * (rd.randint(50,70)/100)
                return betting_money
            elif z_score == 70:
                betting_money = self.money * (rd.randint(30,60)/100)
                return betting_money
            elif z_score == 60:
                betting_money = self.money * (rd.randint(20,50)/100)
                return betting_money
            elif z_score == 50:
                betting_money = self.money * (rd.randint(10,40)/100)
                return betting_money
            elif z_score == 40:
                betting_money = self.money * (rd.randint(10,40)/100)
                return betting_money
            elif z_score == 30:
                betting_money = self.money * (rd.randint(10,40)/100)
                return betting_money
            else:
                betting_money = self.money * (rd.randint(10,30)/100)
                return betting_money
        
    def minus_money(self, x): #class에 저장된 돈 삭감
        self.money = self.money - x

    def actions(self, bet_money,z_score):
        while True:
            if self.say_fold == True:
                return bet_money
            else:
                if z_score >= 70 and (bet_money / self.money)*100 >= 50 : #레이즈_1
                    bet_money = bet_money + (self.money / 4)
                    return bet_money
                elif z_score >= 30 and (bet_money / self.money)*100 >= 20: #레이즈_2
                    bet_money = bet_money + (self.money / 4)
                    return bet_money
                
<<<<<<< HEAD
                elif z_score >= 30 and (bet_money / self.money)*100 >= 20:
=======
                elif z_score <= 30 and (bet_money / self.money)*100 >= 60: #폴드
                    self.say_fold = True
                    return bet_money
                
                else:
                    self.say_call = True
                    return bet_money # 콜
                

>>>>>>> ff8bce1e260210a0de904669defa0d029e574fff
                    



                    




        