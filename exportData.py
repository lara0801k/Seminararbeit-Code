import lxml
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

# leerer String für reinen Text
pure_text = ""

# über alle JSON Files iterieren

for i in range(1, 33):

    # Daten einlesen
    dir = "ressources/response" + f"{i:02d}" + ".json"
    print(dir)
    data = pd.read_json(dir)

    # Spalte content rendered speichern (unsere Daten)
    column_content = data["content"]
    only_content = column_content.apply(lambda x: x["rendered"])

    # HTML entfernen
    for s in range(len(only_content)):
       if only_content[s] != "":
           try:
                article = lxml.html.fromstring(only_content[s]).text_content()
                pure_text += article
           except(html.etree.ParserError, TypeError) as e:
                print(f"Fehler beim Parsen des Inhalts an Index {s}: {e}")

    pure_text = pure_text.strip()
    print(len(pure_text))

# Data Preprocessing
# 1. Noise Removal
characters = '[\.\,\:\;\!\?\"\&\'\)\(\-\‘\–\„\“]'
text_without_characters = re.sub(characters, '', pure_text)
# print('Text ohne Satzzeichen: ', text_without_characters)

# 2. Tokenization
tokenized = word_tokenize(text_without_characters)
# print('Text zerstückelt: ', tokenized)

# Text Normalization
# 3. Stemming
#stemmer = PorterStemmer()
#stemmed = [stemmer.stem(token) for token in tokenized]
# print('Affixe entfernt: ', stemmed)

# 4. Lemmatization
#lemmatizer = WordNetLemmatizer()
#lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]
#print('Lemmatisierung: ', lemmatized)

# 5. Stopword Removal
#stop_words = set(stopwords.words('german'))
#text_without_stopwords = [word for word in tokenized if word not in stop_words]
#print('Stop words entfernt: ', text_without_stopwords)

print(tokenized)