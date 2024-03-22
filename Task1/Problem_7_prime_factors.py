num = int(input())
factors = set()

for prime_num in range(2, num + 1):
    while num % prime_num == 0:
        factors.add(prime_num)
        num //= prime_num

if len(factors) == 0:
    print("Prime Factors: None")
else:
    print("Prime Factors:", ', '.join(map(str, factors)))
