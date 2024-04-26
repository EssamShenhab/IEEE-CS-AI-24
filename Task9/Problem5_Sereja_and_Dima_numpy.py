import numpy as np

# Number of cards
n = int(input())

cards = np.array(list(map(int, input().split())))

sereja_points = 0
dima_points = 0

left = 0
right = n - 1

sereja_turn = True

while left <= right:
    # sereja's turn
    if sereja_turn:
        selected_card = max(cards[left], cards[right])
        sereja_points += selected_card

        if cards[left] > cards[right]:
            left += 1
        else:
            right -= 1
    # Dima's turn
    else:
        selected_card = max(cards[left], cards[right])
        dima_points += selected_card

        if cards[left] > cards[right]:
            left += 1
        else:
            right -= 1

    # Switch turns for the next iteration
    sereja_turn = not sereja_turn

print(sereja_points, dima_points)
