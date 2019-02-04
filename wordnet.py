from textblob import Word
word = Word("tree")
word.synsets[:5]

word.definitions[:5]
#print(word.definitions[:5])
term_h_0 = word.synsets[0]
term_h_1 = word.synsets[1]
term_h_2 = word.synsets[2]
# term_h_0.lemma_names
# term_h_1.lemma_names
# tterm_h_2.lemma_names

print("TREE")
print("hyperonymy is-a")
print(term_h_0.hypernyms())
print(term_h_1.hypernyms())
# print(term_h_2.hypernyms())
print()
print("meronymic part of")
term_m_0 = word.synsets[0]
# term_m_1 = word.synsets[1]
# term_m_2 = word.synsets[2]
print(term_m_0.part_meronyms())
# print(term_m_1.part_meronyms())
# print(term_m_2.part_meronyms())
