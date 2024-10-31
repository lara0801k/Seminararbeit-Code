import pandas as pd
import lxml
from lxml import html

pure_text = ""

# Daten einlesen
data = pd.read_json("ressources/response01.json")

# Spalte content rendered speichern (unsere Daten)
column_content = data["content"]
only_content = column_content.apply(lambda x: x["rendered"])

# HTML entfernen
for i in range(len(only_content)):
   if only_content[i]:
       article = lxml.html.fromstring(only_content[i]).text_content()
       pure_text += article

print(len(pure_text))
pure_text = pure_text.strip()
print(pure_text)