import numpy as np

while True:
    try:
        n = int(input("Enter an integer value: "))
        if 100 >= n >= 0:
            break
        else:
            print("Please enter a non-negative integer value between 0 and 100.")
    except ValueError:
        print("Please enter an integer value")

np1 = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        np1[i, j] = j + 1
print(np1)
