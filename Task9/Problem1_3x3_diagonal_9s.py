import numpy as np

# First solution
# np1 = np.array([[9,0,0],[0,9,0],[0,0,9]])
# print(np1)

# Second solution
# np1 = np.zeros((3, 3), dtype=int)
# for i in range(3):
#     np1[i, i] = 9
# print(np1)


# Third solution
np1 = np.zeros((3, 3), dtype=int)
np.fill_diagonal(np1, 9)
print(np1)
