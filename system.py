from collections import Counter

def show_community_card(a, community_cards):  # a = 차례수
    for i in range(0, 2 + a):
        print(f'{community_cards[i]}', end=' ')

def determine_jokbo(user_card, community_card):
    # 카드 합치기
    total_card = user_card + community_card
    rank_order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A','2','3','4','5']  # 스트레이트 체크용
    rank_order_2 = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']  # 일반 비교용

    # 1. Royal Flush
    for suit in ["Spade", "Hearts", "Diamonds", "Cloba"]:
        if all((r, suit) in total_card for r in ['T','J','Q','K','A']):
            return 'Royal Flush'

    # 2. Straight Flush
    for suit in ["Spade", "Hearts", "Diamonds", "Cloba"]:
        suited = [rank for (rank, s) in total_card if s == suit]
        for i in range(0, 13):
            if all(rank_order[i + j] in suited for j in range(5)):
                return 'Straight Flush'

    # 3. Four of a Kind
    total_ranks = [rank for (rank, suit) in total_card]
    counter = Counter(total_ranks)
    for r in rank_order_2:
        if counter[r] == 4:
            return 'Four of a Kind'

    # 4. Full House
    three = [r for r in rank_order_2 if counter[r] >= 3]
    pair = [r for r in rank_order_2 if counter[r] >= 2 and r not in three]
    if three and pair:
        return 'Full House'

    # 5. Flush
    suit_counter = Counter([suit for (rank, suit) in total_card])
    if any(v >= 5 for v in suit_counter.values()):
        return 'Flush'

    # 6. Straight
    unique_ranks = sorted(set(total_ranks), key=lambda r: rank_order.index(r))
    for i in range(len(rank_order) - 4):
        if all(rank_order[i + j] in unique_ranks for j in range(5)):
            return 'Straight'

    # 7. Three of a Kind
    for r in rank_order_2:
        if counter[r] == 3:
            return '3 of a Kind'

    # 8. Two Pairs
    pairs = [r for r in rank_order_2 if counter[r] == 2]
    if len(pairs) >= 2:
        return '2 Pairs'

    # 9. One Pair
    if 2 in counter.values():
        return '1 Pair'

    # 10. High Card
    max_card = max(total_card, key=lambda card: rank_order_2.index(card[0]))
    return ('High Card', max_card)
