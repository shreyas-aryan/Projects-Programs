#POS TAGGING
import nltk
#nltk.download("punkt")
#nltk.download("averaged_perceptron_tagger")
from nltk.tokenize import word_tokenize
st="The quick brown fox jumps over the lazy dog."
tokens=word_tokenize(st)
tags=nltk.pos_tag(tokens)
print(tags)

#NER
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
st="Sachin Tendulkar lives in Mumbai and worked with Microsoft."
tokens=nltk.word_tokenize(st)
tags=nltk.pos_tag(tokens)
ner=nltk.ne_chunk(tags)
print(ner)
