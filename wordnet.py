from textblob import Word
word = Word("cat")
word.synsets[:5]

word.definitions[:5]
#print(word.definitions[:5])
term0 = word.synsets[0]
term1 = word.synsets[1]
term2 = word.synsets[2]
term0.lemma_names
term1.lemma_names
term2.lemma_names
term1.hypernyms()
print("CAT")
print(term0.hypernyms())
print(term1.hypernyms())
print(term2.hypernyms())
