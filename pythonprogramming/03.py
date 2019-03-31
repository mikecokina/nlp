from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]
stemmed_words = [ps.stem(w) for w in example_words]
print(stemmed_words)


new_text = "It is important to by very pythonly while you are pythoning with python. " \
           "All pythoners have pythoned poorly at least once."
words = word_tokenize(new_text)
stemmed_words = [ps.stem(w) for w in words]
print(stemmed_words)
