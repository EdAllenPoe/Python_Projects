
word_list = ['hello','world','my','name','is','Anna']

letters = set('o')

newlist=list()

for word in word_list:
    if letters & set(word):
        newlist.append(word)
print newlist
