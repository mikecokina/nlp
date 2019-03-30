from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words("english"))
words = word_tokenize(example_sent)
filtered_sentence = [w for w in words if w not in stop_words]
