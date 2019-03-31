from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("geese"))

print(lemmatizer.lemmatize("better", pos="a"))  # 'a' - adjective
print(lemmatizer.lemmatize("best", pos="a"))


print(lemmatizer.lemmatize("run", pos="v"))


