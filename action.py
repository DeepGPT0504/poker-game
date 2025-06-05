import First

class player_poker(): #player가 사용하는 행동

    def __init__(self, player_name, money):
        self.player_name = str(player_name)
        self.money = int(money)

    def betting(self):
        question = input(f'베팅하시겠습니까?(Y/N):').lower()
        if question == 'y':
            while True:
                try:
                    question_2 = int(input(f'얼마를 베팅하시겠습니까?(현재 잔액: {self.money}):'))
                    if question_2 <= self.money:
                        print(f'{question_2}만큼 베팅되었습니다(현재 잔액: {self.money-question_2})')
                        self.money -= question_2
                        break
                    else:
                        print('잔액이 부족합니다')
                except ValueError:
                    print('숫자를 입력해주세요')
        else:
            print('턴을 넘깁니다')

class computer_poker(): #computer_player가 사용하는 행동

    def __init__(self, player_name, money, z_score):
        self.player_name = player_name
        self.money = money
        self.z_score = z_score



        