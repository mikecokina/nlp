from nltk.tokenize import sent_tokenize, word_tokenize


exmaple_text = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. " \
               "The sky is pinkish-blue. You shouldn't eat cardboard."

# x = sent_tokenize(exmaple_text)
# print(x)
# y = word_tokenize(exmaple_text)
# print(y)


for i in word_tokenize(exmaple_text):
    print(i)
