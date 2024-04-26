import numpy as np

j = 0
k = 2
np1 = np.zeros((4, 4), dtype=int)
for i in range(4):
    for j in range(4):
        np1[i, j] = k
        k += 2
print(np1)

mean_value = np.mean(np1)
std_value = np.std(np1)

filtered = (np1 > (mean_value - 0.5 * std_value)) & (np1 < (mean_value + 0.5 * std_value))
print(np1[filtered])
