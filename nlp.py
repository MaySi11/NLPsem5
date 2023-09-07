
# for nlp and regular expression
import modu as nlp
import nltk
import spacy
import en_core_web_sm
from samples import mergeds

# from nltk.tokenize import word_tokenize
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.sem.relextract import extract_rels, rtuple
import string
import re

# for word cloud
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


import sys

from Matrices import Matrics

filename = sys.argv[1]

# read file
text = ""
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

temp = text

# Preprocessing
text = nlp.convert_lower(text)
text = nlp.remove_symbols(text)
text = nlp.tokenize(text)
text = nlp.remove_url(text)
text = nlp.lemment(text)

# Tokenization
T1 = word_tokenize(text)
nlp.tok_vs_freq(T1)

# raw word cloud
nlp.make_cloud(T1)

# word cloud without stopwords
stopwords = set(STOPWORDS)
Temp = T1
T1 = nlp.remove_stop(T1,stopwords)
nlp.make_cloud(T1)

nlp.length_vs_freq(Temp)
nlp.length_vs_freq(T1)

# POS tagging
Tags=nlp.pos_tag_penn(T1)

# Tag Distribution
nlp.tag_dist(Tags)

nouns = nlp.nounSep(Tags)
print("*********nouns********")
print(len(nouns))

verbs = nlp.verbSep(Tags)
print("*********verbs********")
print(len(verbs))

noun_cat=nlp.getCat(nouns)
verb_cat=nlp.getCat(verbs)

print(nouns[10])
print(noun_cat[10][:])

noun_sup,verb_sup=nlp.all_cat(nouns,verbs)

nlp.pltNoun(noun_sup)
nlp.pltVerb(verb_sup)

for x in mergeds:
    x = nlp.convert_lower(x)
    x = nlp.remove_symbols(x)
    x = nlp.tokenize(x)
    x = nlp.remove_url(x)
    x = nlp.lemment(x)
    nlpp = en_core_web_sm.load()
    article = nlpp(x)
    for x in article.ents:
        print("Text: ",x.text,"\tLabel: ",x.label_)
    per, org, loc = nlp.entity_recognition(article.ents)
    print("*********PERSON*********")
    print(per)
    print("*********ORG*********")
    print(org)
    print("*********LOC*********")
    print(loc)



nlpp = en_core_web_sm.load()
article = nlpp(text[:1000000])
print(article.ents)




per = []
org = []
loc = []
nlpp = en_core_web_sm.load()
article = nlpp(text)
p,o,l=nlp.entity_recognition(article.ents)
per.extend(p)
org.extend(o)
loc.extend(l)

article = nlpp(text[1000000:2000000])
p,o,l=nlp.entity_recognition(article.ents)
per.extend(p)
org.extend(o)
loc.extend(l)

article = nlpp(text[2000000:])
p,o,l=nlp.entity_recognition(article.ents)
per.extend(p)
org.extend(o)
loc.extend(l)

print("Person")
print(len(per))

print("Organization")
print(len(org))

print("Location")
print(len(loc))

sentences = nltk.sent_tokenize(temp)
tokanized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokanized_sentences]

print("-------------------PER-LOC-------------------------")
BELONG = re.compile(r'.*\bin|from|belonged|lived\b.*')

for i,sent in enumerate(tagged_sentences):
    sent=ne_chunk(sent)
    rels=extract_rels('PER','GPE',sent,corpus='ace',pattern=BELONG,window=10)
    for rel in rels:
        print(rtuple(rel))

print("-------------------PER-PER-------------------------")
RELATIONS = re.compile(r'.*\bmother|father|sister|brother|aunt|uncle\b.*')

for i,sent in enumerate(tagged_sentences):
    sent = ne_chunk(sent)
    rels = extract_rels('PER', 'PER', sent, corpus = 'ace', pattern = RELATIONS, window = 10)
    for rel in rels:
        print(rtuple(rel))


print("-------------------PER-ORG-------------------------")
ORG = re.compile(r'.*\bwork|of|in\b.*')

for i,sent in enumerate(tagged_sentences):
    sent = ne_chunk(sent)
    rels = extract_rels('PER', 'ORG', sent, corpus = 'ace', pattern = ORG, window = 10)
    for rel in rels:
        print(rtuple(rel))


