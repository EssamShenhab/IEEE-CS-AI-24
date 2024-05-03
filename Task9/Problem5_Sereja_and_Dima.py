while True:
    try:
        n = int(input())
        if 100 >= n >= 0:
            break
        else:
            print("Please enter a non-negative integer value between 0 and 100.")
    except ValueError:
        print("Please enter an integer value")

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
