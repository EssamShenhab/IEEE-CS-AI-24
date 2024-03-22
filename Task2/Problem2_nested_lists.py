if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        scores = float(input())
        python_students.append([name, scores])
    score = [x[1] for x in python_students]
    min_python_students = sorted(set(score))
    student = sorted([y[0] for y in python_students if y[1] == min_python_students[1]])
    for k in student:
        print(k)
