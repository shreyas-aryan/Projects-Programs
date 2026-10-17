import nltk
grammar=nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N | NP PP
VP -> V NP | VP PP
PP -> P NP
Det -> 'the' | 'a'
N -> 'child' | 'cake' | 'fork'
V -> 'ate'
P -> 'with'
""")
parser=nltk.ChartParser(grammar)
sen="the child ate a cake with a fork".split()
for tree in parser.parse(sen):
    print(tree)
    tree.pretty_print()
    tree.draw()
