import random as rd

class player_action(): #player가 사용하는 행동

    def __init__(self, player_name, money, deck):
        self.player_name = str(player_name)
        self.money = int(money)
        self.deck = deck

    def betting(self):
        question = input(f'베팅하시겠습니까?(Y/N):').lower()
        if question == 'y':
            while True:
                try:
                    question_2 = int(input(f'얼마를 베팅하시겠습니까?(현재 잔액: {self.money}):'))
                    if question_2 <= self.money:
                        print(f'{question_2}만큼 베팅되었습니다(현재 잔액: {self.money-question_2})')
                        self.money -= question_2
                        return question_2
                    else:
                        print('잔액이 부족합니다')
                except ValueError:
                    print('숫자를 입력해주세요')
        else:
            print('턴을 넘깁니다')
            return -1
        
    def back_money(self): #class에 저장된 금액 반환
        return self.money


    


class computer_action(): #computer_player가 사용하는 행동

    def __init__(self, player_name, money):
        self.player_name = player_name
        self.money = money

    def cal_betting_momney(self, z_score):
        x = rd.randint(0,10)

        if z_score <= 30 and x <= 7: #손 패가 원 페어 이하일 때 30% 확률로 컴퓨터가 거짓 베팅을 시도한다
            betting_money = self.money * (rd.randint(40,80)/100)
            return betting_money
        elif z_score >= 60 and x <= 6: #손 패가 스트레이트 이상일 때 40% 확률로 거짓 베팅을 시도한다
            betting_money = self.money * (rd.randint(10,40)/100)
            return betting_money
        else: #정석 베팅팅
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
        




        