from main_game import user
from system import determine_jokbo, z_score_jokbo

#1)planoffirst파일에서 정보 정리
my_hand = user_deck
flop = community_cards[:3]


#2) 플레이어 및 공유카드 5개중 3개 공개 (Player 1 = 나)
print("나의 카드 (Player 1)", my_hand)
print("공개된 커뮤니티 카드", flop)

def get_z(my_hand, flop):    
    #3) 족보 판별 시스템
    result = determine_jokbo(my_hand, flop)
    print("현재 게임 나의 카드로 가능한 족보중 가장 순위가 높은 것:", result)

    #4) 족보 기반 점수 판별 시스템
    result_key = result
    score = z_score_jokbo.get(result_key, 0)()
    print(f"당신의 족보 점수는 {score}이며, 이를 바탕으로 배팅하세요!")
