if __name__ == '__main__':
    numbers = []
    N = int(input())
    for _ in range(0, N):
        function, *args = input().split()
        if function == "insert":
            i, e = map(int, args)
            numbers.insert(i, e)
        elif function == "print":
            print(numbers)
        elif function == "remove":
            e = int(args[0])
            numbers.remove(e)
        elif function == "append":
            e = int(args[0])
            numbers.append(e)
        elif function == "sort":
            numbers.sort()
        elif function == "pop":
            numbers.pop()
        elif function == "reverse":
            numbers.reverse()
