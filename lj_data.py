# SIU KING WAI SM4701 Deepstory
# to "normalize" metadata.csv so that punct like :; won't go away because they are not in vocab of dctts
import pandas as pd
import csv
import re
from unidecode import unidecode


# modified from nlp.py
def process(text):
    replace_list = [
        [r'\(|\)|:|;|(\s*-+\s+)|(\s+-+\s*)|\s*-{2,}\s*', ', '],
        [r'\s*,[^\w]*,\s*', ', '],  # capture multiple commas
        [r'\s*,\s*', ', '],  # format commas
    ]
    processed_text = unidecode(text)  # Get rid of the accented characters
    for regex, replacement in replace_list:
        processed_text = re.sub(regex, replacement, processed_text)
    processed_text = re.sub(r'\s+', ' ', processed_text).strip()
    return processed_text


df = pd.read_csv('metadata.csv', encoding='utf-8', sep='|', header=None, quoting=csv.QUOTE_NONE).fillna('')
df[2] = df[2].apply(process)
df.to_csv('lj_fixed.csv', encoding='utf-8', index=False, header=False, sep='|', quoting=csv.QUOTE_NONE)
print('done')
