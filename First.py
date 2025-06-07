import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from planoffirst import ranks, suits, deck
#카드 52장에 대한 경우의 수 random 설정


#플레이어 수 설정
num_players = 4
print(f"플레이어 수: {num_players}명")

#플레이어에게 카드를 2장씩 배분
players = { }
for i in range(1, num_players +1):
    give_deck = [deck.pop() for _ in range(2)]
    players[f'Player {i}'] = give_deck

#공유카드=community card 5개를 설정
community_cards = [deck.pop() for _ in range(5)]

#리스트로서 플레이어 4명의 덱 (각 2장) 터미널에 띄우는 코드
print((" 플레이어 4명의 덱: "))
for name, give_deck in players.items():
    print(f"{name}: {give_deck}")

#총 공유카드 5개중 첫 배팅 후에는 3개만이 공개됨.
print(f" 첫 배팅 후 공개된 공유카드 3장: {community_cards[:3]}")

#카드를 그리는 함수
def draw_card(ax, x, y, rank, suit, color='black'):
    width, height = 0.8, 1.2
    ax.add_patch(Rectangle((x,y), 0.64, 1.3, fill=True, edgecolor='black', facecolor='white', linewidth=2))
    ax.text(x+0.09, y+ height - 0.3, rank, fontsize= 9, color=color)
    ax.text(x+ 0.09, y + height -0.6, suit, fontsize = 7, color=color ) #x,y좌표랑 fontsize 조절로 카드 크기와 위치 조절 가능능
#카드 색=(red = 'heart', 'diamond', black = 'cloba', 'spare')
def get_color(suit):
    return 'red' if suit in ['Hearts', 'Diamonds'] else 'black'

#matplotlib기반 화면창 2d 게임 틀 set 설정
fig, ax = plt.subplots(figsize=(10,10))
ax.set_xlim(0,10)
ax.set_ylim(0, 10)
ax.axis('off')

#플레이어와 카드 위치 설정
positions = {
    'Player 1': {'x': 4.2, 'y': 7, 'dx': 1.0, 'dy': 0, 'name_offset': 0.5, 'name_pos': 'above'},
    'Player 2': {'x': 9, 'y': 2.2, 'dx': 0, 'dy': 1.6, 'name_offset': 1.6, 'name_pos': 'left'},
    'Player 3': {'x': 4.0, 'y': 0.6, 'dx': 1.2, 'dy': 0, 'name_offset': -0.7, 'name_pos': 'below'},
    'Player 4': {'x': 0.2, 'y': 2.2, 'dx': 0, 'dy': 1.6, 'name_offset': -1.6, 'name_pos': 'right'}
}

for player_name, hand in players.items():
    pos = positions[player_name]
    x0, y0 = pos['x'], pos['y']
    dx, dy = pos['dx'], pos['dy']

    # 카드 2장 그리기
    for i, (rank, suit) in enumerate(hand):
        draw_card(ax, x0 + dx * i, y0 + dy * i, rank, suit, get_color(suit))

    # 이름 위치 계산
    if pos['name_pos'] == 'above':
        ax.text(x0, y0 + 1.5, player_name, ha='center')
    elif pos['name_pos'] == 'below':
        ax.text(x0, y0 - 0.9, player_name, ha='center')
    elif pos['name_pos'] == 'left':
        ax.text(x0 + 2, y0 +2 , player_name, rotation=90, va='center')
    elif pos['name_pos'] == 'right':
        ax.text(x0 - 2, y0 +2, player_name, rotation=270, va='center')


for i, (rank, suit) in enumerate(community_cards):
        draw_card(ax, 2.4 + i * 1.1, 4.2, rank, suit, get_color(suit))
ax.text(4.8, 3.6, "Commuinity Cards", fontsize=12, ha = 'center')


plt.tight_layout()
plt.show()

