num = int(input())
divisors = 0
for i in range(1, num):
    if num % i == 0:
        divisors += i
if num == divisors:
    print(f"{num} is a perfect number.")
else:    
        print(f"{num} isn't a perfect number.")