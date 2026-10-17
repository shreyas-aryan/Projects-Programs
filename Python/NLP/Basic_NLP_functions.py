#TOKENIZATION, STOPWORDS, FREQDIST, STEMMER, LEMMATIZER, NORMALIZATION
#import nltk
#nltk.download("punkt")
#nltk.download("stopwords")
#nltk.download("wordnet")
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
#bringing in a string aka content to be worked on
with open("C:/Users/Shreyas/Downloads/file1.txt","r") as file:
    c=file.read()
    print(c)
#normalization so tht words are not treated differently tht have the same meaning but different cases
c=c.lower()
#tokenization sen first
s=sent_tokenize(c)
#word tokenization
tokens=word_tokenize(c)
print(s)
print(tokens)
#now removing the stopwords and punctuation for cleaning
#loading up the english stopwords
stopword=set(stopwords.words("english"))
#create list for the cleaned tokens
cleaned=[]
#follow the logic of checking every word in the tokens and check
#if those words are not stopwords and punct, if they are not then appened it in the list, or else discard
for word in tokens:
    if word not in stopword and word not in string.punctuation:
        cleaned.append(word)
print(cleaned)
#now freqdist of cleaned tokens
f=FreqDist(cleaned)
print(f.most_common(5))
#create empty var w calling porterstemmer for stemming
stemmer=PorterStemmer()
st=[]
#same logic as cleaned tokens printing
for word in cleaned:
    stemmed=stemmer.stem(word)
    st.append(stemmed)
    if word!=stemmed:
        print(f"{word} : {stemmed}")
print()
#lemmatization same logic as stemming
lemmatizer=WordNetLemmatizer()
l=[]
for word in cleaned:
    lemmatized=lemmatizer.lemmatize(word)
    l.append(lemmatized)
    if word!=lemmatized:
        print(f"{word} : {lemmatized}")
#output printing
print(f"\n\nWORD\t\t STEMMED\t\t LEMMATIZED")
for i in range(len(cleaned)):
    token=cleaned[i]
    value=st[i]
    lem=l[i]
    if token!=value or token!=lem:
        print(f"{token}\t\t {value}\t\t  {lem}")
