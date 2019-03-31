import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

# thsi gonna train PunktSentenceTokenizer on train text
custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for idx, sentence in enumerate(tokenized):
            words = nltk.word_tokenize(sentence)
            tagged = nltk.pos_tag(words)

            # named_entity = nltk.ne_chunk(tagged)
            named_entity = nltk.ne_chunk(tagged, binary=True)
            named_entity.draw()

    except Exception as e:
        print(str(e))

process_content()
