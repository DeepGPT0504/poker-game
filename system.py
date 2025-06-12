
def show_community_card(a, community_cards): # a = 차례수

    for i in range(0,2 + a):
        print(f'{community_cards[i]}',end='')


def determine_jokbo(user_card,community_card): # 손패와 커뮤니티 카드를 보고 어느 족보에 해당하는지 결정한 후 해당하는 족보명를 반환
    
    #개인 카드와 커뮤니티 카드를 정리
    total_card = user_card + community_card
    rank_order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A','2','3','4','5'] # 연결된 순서 판단
    rank_order_2 = ['2','3','4','5','6','7','8','9','T','J','Q','K','A',] # 일치 판단
   
    #Royal Flush 판단
    for suit in ["Spade", "Hearts", "Diamonds", "Cloba"]:
        if ('T',suit) in total_card and ('J',suit) in total_card and ('Q',suit) in total_card and ('K',suit) in total_card and ('A',suit) in total_card:
            return ('Royal Flush')
        
    #Straight Flush 판단
    for suit in ["Spade", "Hearts", "Diamonds", "Cloba"]:
        for i in range(0,13):
              if (rank_order[i],suit) in total_card and (rank_order[i+1],suit) in total_card and( rank_order[i+2],suit) in total_card and (rank_order[i+3],suit)in total_card and (rank_order[i+4],suit) in total_card:
                    return ('Straight Flush')
    #4 of a kind 판단
    for i in range(0,13):
        if (i,"Spade") in total_card and (i,"Hearts") in total_card and (i,"Diamonds") in total_card and (i,"Cloba") in total_card:
              return ('4 of a kind')
        
    #족보 상관 없이 숫자로만 패를 나누는 'Full House','Straight','3 of kind','2 Pairs','1 Pair'는 숫자 모음을 만들어서 판별
    total_ranks = [ rank for (rank,suit) in total_card]
    
    #Full House 판단
    total_ranks_Full = total_ranks.copy() #Full house 판단에서만 쓰일 랭크 모음
    for i in range(0,13):
        counting = total_ranks_Full.count(rank_order[i])
        if counting >= 3:
            total_ranks_Full.remove(rank_order[i])
            for i in range(0,13):
                counting = total_ranks_Full.count(rank_order[i])
                if counting >= 2:
                     return ('Full House')
                
    #Straight 판단
    for i in range(0,13):
         if rank_order[i] in total_card and rank_order[i+1] in total_card and rank_order[i+2] in total_card and rank_order[i+3] in total_card and rank_order[i+4] in total_ranks:
              return ('Straight')
         
    #3 of kind 판단
    for i in range(0,13):
        counting = total_ranks.count(rank_order_2[i])
        if counting >= 3:
             return ('3 of kind')
        
    #2 Pairs 판단
    total_ranks_2 = total_ranks.copy() #2 Pairs 판단에서만 쓰일 랭크 모음
    for i in range(0,13):
        counting = total_ranks_2.count(rank_order_2[i])
        if counting >= 2:
            total_ranks_2.remove(rank_order_2[i])
            for i in range(0,13):
                counting = total_ranks_2.count(rank_order_2[i])
                if counting >= 2:
                     return ('2 Pairs')
                
    #1 Pair 판단
    for i in range(0,13):
        counting = total_ranks.count(rank_order_2[i])
        if counting >= 2:
             return ('1 Pair')
        
    #High Card 판단
    max_card = max(total_card, key=lambda card: rank_order_2.index(card[0]))
    return 'High Card'

def get_z(user_deck, community_card):    

    z_score_jokbo = {
     'Royal Flush': 100,
     'Straight Flush': 90,
     '4 of a kind': 80,
     'Full House': 70,
     'Straight': 60,
     '3 of a kind': 50,
     '2 Pairs': 40,
     '1 Pair': 30,
     'High Card': 10
    }

    result = determine_jokbo(user_deck, community_card)
    
    if isinstance(result, tuple):
        result = result[0]
    
    return z_score_jokbo[result]

#각 round에서 베팅 단계를 수행하는 함수
def round_betting(starting_bet_money, players, z_scores,user,bank):
    current_bet = starting_bet_money
    num_players = len(players)
    player_bets = [0] * num_players
    order = 0

    print(f"\n[베팅 라운드 시작] 시작 판돈: {current_bet}, [총 판돈]: {bank}\n")

    while True:
        player = players[order]

        if player.say_fold:
            print(f"{player.player_name}는 이미 폴드했습니다.")

        elif player.money == 0:
            print(f'{player.name}님은 이미 올인하셨습니다')
            
        else:
            # 사람과 컴퓨터 분기 처리
            if player == user:
                action_result = player.actions(current_bet)
            else:
                z_score = z_scores[order]
                action_result = player.actions(current_bet, z_score,bank)

            # 행동 반영
            if player.say_fold:
                print(f"{player.player_name}가 폴드했습니다.")
                player_bets[order] = 0
            
            elif player.say_call:
                call_amount = current_bet - player_bets[order]
                print(f"{player.player_name}가 콜했습니다. {call_amount} 만큼 추가 지불")
                player.money -= call_amount
                player_bets[order] = current_bet
            
            elif player.say_raise:
                raise_amount = action_result - current_bet
                print(f"{player.player_name}가 레이즈했습니다! {raise_amount} 만큼 판돈 증가")
                player.money -= raise_amount
                current_bet = action_result
                player_bets[order] = current_bet

        # 라운드 종료
        active_bets = [player_bets[i]  for i in range(num_players) if players[i].say_fold != True]
        if len(active_bets) >= 2 and all(bet == current_bet for bet in active_bets):
            print("\n[베팅 라운드 종료]\n")
            break

        order = (order + 1) % num_players

    return current_bet #플레이어들이 베팅으로 올린 현재 베팅가를 반환










            
        


    


    






              
                

    
        
        
        
        

        