i = int(input())
sum = 1

if i == 0:
    print(1)
elif i < 0 :
    print("invalid input")   
else:
    for n in range(1, i+1):
        sum *=  n
    print(sum)