import lxml
import spacy
from lxml import html
import pandas as pd
import re
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os
import json
from lxml.html import HTMLParser

text = '<h1> Hallo Paul, dies ist ein kurzer Beispieltext. Wie geht es dir? <h1>, größer, große, Tester, gehst, ging, gegangen, Katzen'

# HTML-Tags entfernen
article_without_html_tags = lxml.html.fromstring(text).text_content()
print("HTML entfernen: ", article_without_html_tags)

# Data Preprocessing
# 1. Noise Removal
characters = '[\.\,\:\;\!\?\"\&\'\)\(\-\‘\–\„\“]'
text_without_characters = re.sub(characters, '', article_without_html_tags)
print('Text ohne Satzzeichen: ', text_without_characters)

# 2. Lowercasing
text_without_characters_lowercase = text_without_characters.lower()
print("Lowercasing: ", text_without_characters_lowercase)

# 3. Tokenization
tokenized = word_tokenize(text_without_characters_lowercase)
print('Text zerstückelt: ', tokenized)

# 4. Stopword Removal
stop_words = set(stopwords.words('german'))
tokens_without_stopwords = [word for word in tokenized if word not in stop_words]
print('Stop words entfernt: ', tokens_without_stopwords)

# Text Normalization
# 5. Stemming
stemmer = PorterStemmer()
tokens_stemmed = [stemmer.stem(token) for token in tokens_without_stopwords]
print('Stemming: ', tokens_stemmed)

# 6. Lemmatization
lemmatizer = WordNetLemmatizer()
tokens_lemmatized_1 = [lemmatizer.lemmatize(token) for token in tokens_without_stopwords]
print('Lemmatisierung mit WordNetLemmatizer: ', tokens_lemmatized_1)

# hierfür muss Großschreibung noch korrekt sein
nlp = spacy.load('de_core_news_sm')
doc = nlp(text_without_characters)
tokens_lemmatized_2 = [token.lemma_ for token in doc]
print('Lemmatisierung mit Spacy:', tokens_lemmatized_2)
# tokens.pos_ gibt Wortart aus
low = [token.lower() for token in tokens_lemmatized_2]

print(low)


# oder Chunking
from nltk.tokenize import sent_tokenize

text = ('Die natürliche Sprachverarbeitung ist ein spannendes Forschungsgebiet der Informatik, '
        'das sich mit der Interaktion zwischen Computern und menschlicher Sprache beschäftigt. '
        'Ziel ist es, Computern das Verstehen und Generieren von natürlicher Sprache zu ermöglichen, '
        'sodass sie effektiver mit Menschen kommunizieren können.')
chunks = sent_tokenize(text, language='german')
print(chunks)