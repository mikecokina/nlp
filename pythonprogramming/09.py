import numpy as np
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample_text = gutenberg.raw("bible-kjv.txt")
tokeniezed = sent_tokenize(sample_text)

print(np.array(tokeniezed[1:50]))
