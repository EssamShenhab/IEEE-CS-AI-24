import numpy as np

n, m = map(int, input().split())

photo = np.array([input().split() for _ in range(n)])

is_colored = np.any((photo != 'W') & (photo != 'w') & (photo != 'B') & (photo != 'b') & (photo != 'G') & (photo != 'g'))

if is_colored:
    print("#Color")
else:
    print("#Black&White")
