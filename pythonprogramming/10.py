from nltk.corpus import wordnet

# synonym set for word `program`
syns = wordnet.synsets("program")

print(len(syns))
print(syns[0])
print(syns[0].lemmas()[0].name())
print(syns[0].definition())
print(syns[0].examples())


synonyms = list()
antonnyms = list()

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        print(l)
        if l.antonyms():
            antonnyms.append(l.antonyms()[0].name())

# print(set(synonyms))
# print(set(antonnyms))

# word similarity
word1 = wordnet.synset("ship.n.01")
word2 = wordnet.synset("boat.n.01")
print(word1.wup_similarity(word2))


word1 = wordnet.synset("ship.n.01")
word2 = wordnet.synset("car.n.01")
print(word1.wup_similarity(word2))


word1 = wordnet.synset("ship.n.01")
word2 = wordnet.synset("cat.n.01")
print(word1.wup_similarity(word2))


word1 = wordnet.synset("sheep.n.01")
word2 = wordnet.synset("cat.n.01")
print(word1.wup_similarity(word2))




