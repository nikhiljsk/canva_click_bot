from itertools import permutations
from collections import defaultdict

multiple = defaultdict(list)

# Read words
with open('words.txt', 'r') as file:
    words = file.read()
words = words.split('\n')

# Read words
with open('all_words.txt', 'r') as file:
    all_words = file.read()
all_words = all_words.split('\n')

for word in words:
    keywords = list(set([''.join(i) for i in permutations(word)]))
    for keyword in keywords:
        if keyword in all_words:
            multiple[word].append(keyword.upper())

all_w = list()
for word in words:
    all_w.append([word] + multiple[word])
print(all_w)