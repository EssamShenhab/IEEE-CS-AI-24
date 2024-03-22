from collections import Counter

words = []
try:
    with open("sample.txt") as file:
        text = file.read()
        print(text)
        words = text.split()
        print(words)

        words_counts = Counter(words)
        for word, count in words_counts.items():
            print(f"{word}: {count}")

except FileNotFoundError:
    print("That file wasn't found")
