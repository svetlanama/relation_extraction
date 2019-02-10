from textblob import Word
from textblob import TextBlob
words = [Word("second"), Word("interval"), Word("time")]
#words = [Word("linear time")]
for x in range(0, len(words)):
    # print("i:", x)
    word = words[x]
    print(">>>>>:", word)
    print("synsets", word.synsets[:5])

    print("\nhyperonymy is-a: ")

    #TODO: check if len(synsets) > 0
    for i in range(0, 3):
        term = word.synsets[i]
        print(term.hypernyms())

    print("\nmeronymic part of")
    print(word.synsets[0].part_meronyms())
    print("\n")

# testimonial = TextBlob("time interval")
# print(">>>>> noun_phrases:", testimonial.noun_phrases)
# print(">>>>>:", testimonial.noun_phrases[0].synsets)
#phrases
