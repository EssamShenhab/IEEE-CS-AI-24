sentence = input()
index = sentence.index(“ ”)
first_word = sentence[:index]
second_word = sentence[index+1:]
print(second_word+ ' ' +first_word)