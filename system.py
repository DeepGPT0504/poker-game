
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
    return ('High Card', max_card)

def get_z(user_deck, community_card):    

    z_score_jokbo = {
     'Royal Flush': 100,
     'Straight Flush': 90,
     '4 of a kind': 80,
     'Full house': 70,
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

def round_betting(order, current_bet_money,player_1, player_2,player_3,player_4):
    player_order = [player_1,player_2,player_3,player_4]
    
    while True:

        if all(player_1.say_call,player_2.say_call,player_3.say_call,player_4.say_call) == True:
             return current_bet_money
        else:
            first_player.actions()
            if second_player.actions() + current_bet_money >= current_bet_money:



            
        


    


    






              
                

    
        
        
        
        

        