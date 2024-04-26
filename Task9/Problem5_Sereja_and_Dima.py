n = int(input())
cards = list(map(int, input().split()))

sereja_points = 0
dima_points = 0
turn = 1

while cards:
    if cards[0] > cards[-1]:
        max_card = cards.pop(0)
    else:
        max_card = cards.pop()

    if turn == 1:
        sereja_points += max_card
        turn = 2
    else:
        dima_points += max_card
        turn = 1

print(sereja_points, dima_points)
