# SIU KING WAI SM4701 Deepstory
from num2words import num2words
from unidecode import unidecode
import re
import fasttext
import spacy
from spacy.tokenizer import Tokenizer
from spacy_syllables import SpacySyllables
from spacy_cld import LanguageDetector as cld
from spacy_langdetect import LanguageDetector as langdetect

lang_model = fasttext.load_model("lid.176.bin")
# All the nlp pipelines
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe(cld())
nlp.add_pipe(langdetect(), name='language_detector', last=True)
tokenizer = Tokenizer(nlp.vocab)
syllables = SpacySyllables(nlp)
nlp.add_pipe(syllables, after='tagger')


def tag_and_process(text):
    # regular expressions for various steps
    attr_list = [
        [r'\d', 'D'],  # Digits
        [r'\*', 'A'],  # Action
        [r'-{2}', 'U'],  # Unfinished
        [r'\?', 'Q'],  # Question
        [r'!', 'E'],  # Exclamation
        [r'\.\.\.|…', 'S'],  # Sigh
        [r'[\w\s]-[\w\s]', 'H']  # Hyphen
    ]
    replace_list = [
        [r'\?!', '?'],
        [r'\*(.+?)\*', ''],
        [r'^(\.\.\.|…)', ''],
        [r'"(\.\.\.|…)', '"'],
        [r'(\.\.\.|…)$', ','],
        [r'(\.\.\.|…)"', ','],
        [r'(\.\.\.|…)\?', '?'],
        [r'(\.\.\.|…)!', '!'],
        [r'\.\.\.|…', ', '],
        [r'--$', '.'],
        [r' - ', ', '],
        [r'-- ', ', '],
        [r' \.', '. '],
        [r'--\?', '?'],
        [r'Vol\.', 'Volume ']
    ]
    num_replace_list = [
        [r'202', 'two-oh-two'],  # just this one specifically
        [r'\d(?:st|nd|rd|th)', lambda x: num2words(x.group()[:-2], to='ordinal')],
        [r'[12][0-9]{3}', lambda x: num2words(x.group(), to='year')],
        [r'\d+', lambda x: f' {num2words(x.group())}'],
        [r' \d+', lambda x: num2words(x.group())]
    ]
    # Replacing
    attr = ''.join([tag for regex, tag in attr_list if re.search(regex, text)])
    processed_text = unidecode(text)  # Get rid of the accented characters
    for regex, replacement in replace_list:
        processed_text = re.sub(regex, replacement, processed_text)
    if 'D' in attr:
        for regex, replacement in num_replace_list:
            processed_text = re.sub(regex, replacement, processed_text)
    # Finalize
    processed_text = re.sub(r'\s+', ' ', processed_text).strip()
    # NLP stuffs
    doc = nlp(text)  # for detecting language in raw text
    tokenized = tokenizer(processed_text)  # for word counts
    syllables_count = sum(filter(None, [token._.syllables_count for token in nlp(processed_text)]))  # for syllables
    return \
        processed_text, \
        attr, \
        len(tokenized), \
        syllables_count, \
        lang_model.predict(text)[0][0][9:], \
        lang_model.predict(processed_text)[0][0][9:], \
        ','.join(doc._.languages), \
        ','.join(tokenized._.languages), \
        doc._.language['language'], \
        tokenized._.language['language']
