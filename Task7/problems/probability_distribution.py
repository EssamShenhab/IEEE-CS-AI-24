from collections import Counter

while True:
    try:
        input_list = input()
        if not input_list.strip():
            raise ValueError("Empty input! Please enter at least one number.")

        data = sorted(list(map(int, input_list.split())))
        counter = Counter(data)
        p = {key: value / len(data) for key, value in counter.items()}
        print(p)
        break
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
