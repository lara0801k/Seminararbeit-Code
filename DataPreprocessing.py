import re

from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

text = 'jene. So many squids are jumping. dieselbe. Hallo. Mein Name ist Lara. Wie geht es dir, Paul? seiner. So viele Leute haben Haustiere. unerreichbar. schlauer. klüger. am besten'
print('Eingegebener Text: ', text)

# 1. Noise Removal
characters = '[\.\,\:\;\!\?\"\&]'
text_without_characters = re.sub(characters, '', text)
print('Text ohne Satzzeichen: ', text_without_characters)

# 2. Tokenization
tokenized = word_tokenize(text_without_characters)
print('Text zerstückelt: ', tokenized)

# Text Normalization
# 3. Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(token) for token in tokenized]
print('Affixe entfernt: ', stemmed)

# 4. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token) for token in tokenized]
print('Lemmatisierung: ', lemmatized)

# 5. Stopword Removal
stop_words = set(stopwords.words('german'))
text_without_stopwords = [word for word in tokenized if word not in stop_words]
print('Stop words entfernt: ', text_without_stopwords)