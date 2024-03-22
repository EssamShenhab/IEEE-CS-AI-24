event_a = [1, 0, 1, 0, 1]
event_b = [1, 1, 0, 0, 1]

p_a_intersect_b = 0
p_a = 0

for i in range(len(event_a)):
    if event_a[i] == event_b[i] == 1:
        p_a_intersect_b += 1
    if event_a[i] == 1:
        p_a += 1

if p_a == 0:
    print(0)
else:
    print(p_a_intersect_b / p_a)
