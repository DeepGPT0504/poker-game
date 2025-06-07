
def show_community_card(a, community_cards): # a = 차례수

    for i in range(0,2 + a):
        print(f'{community_cards[i]}',end='')


def determine_jokbo(user_card,community_card): # 손패와 커뮤니티 카드를 보고 어느 족보에 해당하는지 결정한 후 해당하는 족보명를 반환
    
    #개인 카드와 커뮤니티 카드를 정리
    total_card = []
    total_card.append(i for i in user_card)
    total_card.append(i for i in community_card)
    rank_order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A','2','3','4','5']
   
    #Royal Flush 판단
    for suit in ["Spade", "Hearts", "Diamonds", "Cloba"]:
        if all((suit,'T'),(suit,'J'),(suit,'Q'),(suit,'K'),(suit,'A')) in total_card:
            return 'Royal Flush'
        
    #Straight Flush 판단
    for suit in ["Spade", "Hearts", "Diamonds", "Cloba"]:
        for i in range(0,13):
              if all((suit, rank_order[i]),(suit, rank_order[i+1]),(suit, rank_order[i+2]),(suit, rank_order[i+3]),(suit, rank_order[i+4])) in total_card:
                    return 'Straight Flush'
    #4 of a kind 판단
    for i in range(0,13):
        if all(("Spade", i),("Hearts",i),("Diamonds",i),("Cloba",i)) in total_card:
              return '4 of a kind'
        
    #족보 상관 없이 숫자로만 패를 나누는 'Full House','Straight','3 of kind','2 Pairs','1 Pair'는 숫자 모음을 만들어서 판별
    total_ranks = [ rank for (suit,rank) in total_card]
    
    #Full House 판단
    total_ranks_Full = total_ranks #Full house 판단에서만 쓰일 랭크 모음
    for i in range(0,13):
        counting = total_ranks_Full.count(rank_order[i])
        if counting >= 3:
            del total_ranks_Full[rank_order[i]]
            for i in range(0,13):
                counting = total_ranks_Full.count(rank_order[i])
                if counting >= 2:
                     return 'Full House'
                
    #Straight 판단
    for i in range(0,13):
         if all(rank_order[i],rank_order[i+1],rank_order[i+2],rank_order[i+3],rank_order[i+4]) in total_ranks:
              return 'Straight'
         
    #3 of kind 판단
    for i in range(0,13):
        counting = total_ranks.count(rank_order[i])
        if counting >= 3:
             return '3 of kind'
        
    #2 Pairs 판단
    total_ranks_2 = total_ranks #2 Pairs 판단에서만 쓰일 랭크 모음
    for i in range(0,13):
        counting = total_ranks_2.count(rank_order[i])
        if counting >= 2:
            del total_ranks_2[rank_order[i]]
            for i in range(0,13):
                counting = total_ranks_2.count(rank_order[i])
                if counting >= 2:
                     return '2 Pairs'
                
    #1 Pair 판단
    for i in range(0,13):
        counting = total_ranks.count(rank_order[i])
        if counting >= 2:
             return '1 Pair'
        
    #High Card 판단
    




              
                

    
        
        
        
        

        