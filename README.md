# Install

pip install -r requirements

## Install additional nltk tools (or run first_run.py)
    
    python >> import nltk
    python >> nltk.download()
    
and download ``all``



## Dict

    `tokenizing`:
        word tokenizer - spearation by words 
        sentence tokenizer - separataion by sentence
        
    `corpora` - body of text, e.g. speeach, journal body, etc.
    `lexicon` - dictionary; different types due to different kind of usage (scientific, finanace, regular)
    
    
## Lessons (pythonprogramming)

### `01.py`

Basic word and sentence tokenizing

### `02.py`

This lesson is about stop words. Words thaht to not have any meanig and you can remove them.

### `03.py`

Stemming, method of data preparation (like normalizing method). Looking for word or strip to word that represnt 
couple of different form of same word, e.g. riding, ride, is stemmed to `ride`.

### `04.py`

Related to speech tagging

`PunktSentenceTokenizer` - unsupervised ML tokenizer

Tag list::
    
    POS tag list:
    
    CC	coordinating conjunction
    CD	cardinal digit
    DT	determiner
    EX	existential there (like: "there is" ... think of it like "there exists")
    FW	foreign word
    IN	preposition/subordinating conjunction
    JJ	adjective	'big'
    JJR	adjective, comparative	'bigger'
    JJS	adjective, superlative	'biggest'
    LS	list marker	1)
    MD	modal	could, will
    NN	noun, singular 'desk'
    NNS	noun plural	'desks'
    NNP	proper noun, singular	'Harrison'
    NNPS	proper noun, plural	'Americans'
    PDT	predeterminer	'all the kids'
    POS	possessive ending	parent\'s
    PRP	personal pronoun	I, he, she
    PRP$	possessive pronoun	my, his, hers
    RB	adverb	very, silently,
    RBR	adverb, comparative	better
    RBS	adverb, superlative	best
    RP	particle	give up
    TO	to	go 'to' the store.
    UH	interjection	errrrrrrrm
    VB	verb, base form	take
    VBD	verb, past tense	took
    VBG	verb, gerund/present participle	taking
    VBN	verb, past participle	taken
    VBP	verb, sing. present, non-3d	take
    VBZ	verb, 3rd person sing. present	takes
    WDT	wh-determiner	which
    WP	wh-pronoun	who, what
    WP$	possessive wh-pronoun	whose
    WRB	wh-abverb	where, when

### `05.py`

Chunking in NLTK

### `06.py`

Chinking with NLTK. Basically chunk everything except of something




