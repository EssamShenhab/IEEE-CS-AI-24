def get_numbers():
    numbers_list = []
    while True:
        try:
            numbers = input("Enter some numbers seperated by spaces: ")
            if not numbers.strip():
                print("No numbers entered. Try again.")
                continue
            numbers_list = [float(num) for num in numbers.split()]
            break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

    return numbers_list


def find_min(numbers):
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value


def find_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value


def find_mean(numbers):
    sum_of_numbers = 0
    length = 0
    for number in numbers:
        sum_of_numbers += number
        length += 1
    mean = sum_of_numbers/length
    return mean


def find_mode(numbers):
    num_count = set()
    modes = []
    for number in numbers:
        if number in num_count:
            if number not in modes:
                modes.append(number)
        else:
            num_count.add(number)
    return modes


def find_median(numbers):
    length = 0
    for _ in numbers:
        length += 1
    numbers.sort()
    i = (length + 1) // 2
    if length % 2 == 0:
        return (numbers[i-1]+numbers[i])/2
    else:
        return numbers[i]


def find_range(numbers):
    max_value = find_max(numbers)
    min_value = find_min(numbers)
    range_of_numbers = max_value - min_value
    return range_of_numbers


def find_variance(numbers):
    length = 0
    numerator = 0
    mean = find_mean(numbers)
    for number in numbers:
        numerator += (number - mean)**2
        length += 1
    variance = numerator / (length - 1)
    return round(variance, 2)


def find_STD(numbers):
    variance = find_variance(numbers)
    std = variance**0.5
    return round(std, 7)


def find_Quariles(numbers):
    numbers.sort()
    q2 = find_median(numbers)

    length = 0
    for _ in numbers:
        length += 1

    lower_half = numbers[:length // 2]
    upper_half = numbers[length // 2 + length % 2:]
    half_the_length = 0
    for _ in lower_half:
        half_the_length += 1

    if half_the_length % 2 == 0:
        q1 = (lower_half[half_the_length // 2 - 1] + lower_half[half_the_length // 2]) / 2
        q3 = (upper_half[half_the_length // 2 - 1] + upper_half[half_the_length // 2]) / 2
    else:
        q1 = lower_half[half_the_length // 2]
        q3 = upper_half[half_the_length // 2]

    return q1, q2, q3


def find_IQR(numbers):
    q1, q2, q3 = find_Quariles(numbers)
    iqr = q3 - q1
    return iqr


# ANOTHER SOLUTION TO GET Quartiles AND Interquartile Range (IQR)
# def find_Quariles(numbers):
#     numbers.sort()
#     q2 = find_median(numbers)
#
#     length = 0
#     for _ in numbers:
#         length += 1
#
#     lower_half = numbers[:length // 2]
#     upper_half = numbers[length // 2 + length % 2:]
#     half_the_length = 0
#     for _ in lower_half:
#         half_the_length += 1
#
#     if half_the_length % 2 == 0:
#         q1 = (lower_half[half_the_length // 2 - 1] + lower_half[half_the_length // 2]) / 2
#         q3 = (upper_half[half_the_length // 2 - 1] + upper_half[half_the_length // 2]) / 2
#     else:
#         q1 = lower_half[half_the_length // 2]
#         q3 = upper_half[half_the_length // 2]
#
#     iqr = q3 - q1
#     return q1, q2, q3, iqr
