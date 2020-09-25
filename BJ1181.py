# num = int(input())

# wordsList = []

# for i in range(num):
#     word = input()
#     wordLength = len(word)
#     wordsList.append((word, wordLength))

# wordsList = list(set(wordsList))

# wordsList.sort(key=lambda word: (word[1], word[0]))

# for word in wordsList:
#     print(word[0])
import operator as op

num = int(input())

wordsList = []

for i in range(num):
    word = input()
    wordLength = len(word)
    wordsList.append((word, wordLength))

wordsList = list(set(wordsList))

wordsList.sort(key=op.itemgetter(1, 0))

for word in wordsList:
    print(word[0])
