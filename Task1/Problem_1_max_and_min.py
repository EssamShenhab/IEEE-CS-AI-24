numbers = []
num = 0
while not num == -1:
    num = int(input())
    if num != -1:
        numbers.append(num)
    
print(max(numbers), min(numbers))