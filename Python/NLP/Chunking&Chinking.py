import nltk
from nltk.tokenize import word_tokenize
st="The quick brown fox jumps over the lazy dog."
tokens=word_tokenize(st)
tags=nltk.pos_tag(tokens)
#chunking
grammar="NP: {<DT>?<JJ>*<NN>}"
chunk=nltk.RegexpParser(grammar)
tree=chunk.parse(tags)
print(tree)
tree.draw()
#chinking
gr="""
Chunk: {<.*>+}
        }<JJ>{"""
chink=nltk.RegexpParser(gr)
tree2=chink.parse(tags)
print(tree2)
tree2.draw()
