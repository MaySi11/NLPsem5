# for nlp and regular expression
import nltk
import re
from nltk.corpus import wordnet as wn

# for word cloud
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np

# make lowercase


def convert_lower(text):
    return text.lower()

# remove everything that is not english alphabets and single length chaacters except 'a'


def remove_symbols(text):
    text = re.sub('[\n]', ' ', text)
    text = re.sub('[-]+', '', text)
    text = re.sub('[^A-Za-z ]+', ' ', text)
    text = re.sub(r'(?i)\b[a-z]\b', ' ', text)
    return text


# Tokenize


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    words = [word for word in tokens]
    return ' '.join(words)

# remove urls


def remove_url(text):
    text = re.sub(r"http\S+", "", text)
    return text

# lemmentization


def lemment(text):
    tokens = nltk.word_tokenize(text)
    lemmatizer = nltk.WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in tokens]
    return ' '.join(lemmas)

# making word cloud


def make_cloud(T):
    word_cloud = WordCloud(width=1920*2, height=1080*2, collocations=False,
                           background_color='white', stopwords={}, min_font_size=1).generate(' '.join(T))
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

# removing stop words


def remove_stop(T, stopwords):
    return [word for word in T if word not in stopwords]

# graph plotting


def length_vs_freq(T):
    gset = []
    for i in T:
        gset.append(len(i))
    pd.Series(gset).value_counts().plot(kind='bar')
    plt.title("Length of word Vs Frequency")
    plt.xlabel('Length')
    plt.ylabel("Frequency")
    plt.show()


def tok_vs_freq(T):
    pd.Series(T).value_counts()[:20].plot(kind='bar')
    plt.title("Tokes Vs Frequency")
    plt.xlabel('Tokens')
    plt.ylabel("Frequency")
    plt.show()

# POS tagging
def pos_tag_penn(T):
    tokset = set()
    for i in T:
        tokset.add(i)
    Tags = nltk.pos_tag(tokset)
    return Tags


# Tag Distribution
def tag_dist(T):
    pd.Series(Tag for (word, Tag) in T).value_counts()[:20].plot(kind='bar')
    plt.title("Tags Vs Frequency")
    plt.xlabel('Tags')
    plt.ylabel("Frequency")
    plt.show()


def nounSep(T):
    def is_noun(pos): return pos[:1] == 'N'
    nouns = [word for (word, pos) in T if is_noun(pos)]
    return nouns

def verbSep(T):
    def is_verb(pos): return pos[:1] == 'V'
    verbs = [word for (word, pos) in T if is_verb(pos)]
    return verbs

def getCat (words):
    categories=[]
    for word in words:
        cat=[]
        for synset in wn.synsets(word):
            if(('noun' in synset.lexname ()) & ('Tops' not in synset.lexname()) ):
                cat.append(synset.lexname())
            if('verb' in synset.lexname()) :
                cat.append(synset.lexname())
        categories.append (cat)
    return categories

def all_cat (no,ve):
    nouns=[]
    verbs=[]
    for word in no:
        for synset in wn.synsets (word):
            if(('noun' in synset.lexname()) & ('Tops' not in synset.lexname()) ):
                nouns.append(synset.lexname())
            if('verb' in synset.lexname()):
                verbs.append(synset.lexname())
    for word in ve:
        for synset in wn.synsets (word):
            if(('noun' in synset.lexname()) & ( 'Tops' not in synset.lexname()) ):
                nouns.append(synset.lexname())
            if('verb' in synset.lexname()):
                verbs.append(synset.lexname())
    return nouns, verbs

def pltNoun(nsup):
    freq = {}
    for item in nsup:
        item = item[5:]
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    plt.barh(range(len(freq)), list(freq.values()), align='center')
    plt.yticks(range(len(freq)), list(freq.keys()))
    plt.show()

def pltVerb(vsup):
    freq = {}
    for item in vsup:
        item = item[5:]
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    plt.barh(range(len(freq)), list(freq.values()), align='center')
    plt.yticks(range(len(freq)), list(freq.keys()))
    plt.show()

def entity_recognition (doc):
    person=[]
    org=[]
    location=[]
    for X in doc:
        if (X.label_== 'PERSON') and X.text not in person:
            person.append(X.text)
        if (X.label_== 'ORG') and X.text not in org:
            org.append(X.text)
        if ((X.label_ == 'LOC') or (X.label_ == 'GPE')) and X.text not in location:
            location.append(X.text)
    return person, org, location