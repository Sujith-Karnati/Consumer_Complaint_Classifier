
import re
import html
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet


# Download required NLTK resources
nltk_resources = [
    "stopwords",
    "punkt",
    "punkt_tab",
    "wordnet",
    "omw-1.4",
    "averaged_perceptron_tagger_eng"
]

for resource in nltk_resources:
    nltk.download(resource, quiet=True)


# Initialize NLP components
stop_words = set(stopwords.words("english"))

# Preserve negation words
negation_words = {
    "no", "not", "nor", "never",
    "neither", "none", "cannot"
}

stop_words = stop_words - negation_words

lemmatizer = WordNetLemmatizer()


def clean_text(text):

    if text is None:
        return ""

    text = html.unescape(str(text))
    text = text.lower()

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)

    # Remove URLs
    text = re.sub(
        r'https?://\S+|www\.\S+',
        ' ',
        text
    )

    # Remove email addresses
    text = re.sub(
        r'\b[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}\b',
        ' ',
        text
    )

    # Expand contractions
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "can not", text)
    text = re.sub(r"n't\b", " not", text)
    text = re.sub(r"'re\b", " are", text)
    text = re.sub(r"'ve\b", " have", text)
    text = re.sub(r"'ll\b", " will", text)
    text = re.sub(r"'d\b", " would", text)
    text = re.sub(r"'m\b", " am", text)

    # Preserve decimal numbers
    text = re.sub(
        r'(?<=\d)\.(?=\d)',
        'DECIMALPOINT',
        text
    )

    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # Restore decimal points
    text = text.replace('DECIMALPOINT', '.')

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def remove_stopwords(text):

    words = text.split()

    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    return ' '.join(filtered_words)


def get_wordnet_pos(tag):

    if tag.startswith('J'):
        return wordnet.ADJ

    elif tag.startswith('V'):
        return wordnet.VERB

    elif tag.startswith('N'):
        return wordnet.NOUN

    elif tag.startswith('R'):
        return wordnet.ADV

    else:
        return wordnet.NOUN


def lemmatize_text(text):

    words = word_tokenize(text)

    tagged_words = pos_tag(words)

    lemmatized_words = []

    for word, tag in tagged_words:

        pos = get_wordnet_pos(tag)

        lemma = lemmatizer.lemmatize(word, pos)

        lemmatized_words.append(lemma)

    return ' '.join(lemmatized_words)


def preprocess_complaint(text):

    # Step 1: Clean original complaint
    cleaned = clean_text(text)

    # Step 2: Remove stopwords
    without_stopwords = remove_stopwords(cleaned)

    # Step 3: Lemmatization
    lemmatized = lemmatize_text(without_stopwords)

    # Step 4: Remove masked placeholders
    lemmatized = re.sub(
        r'\bx{2,}\b',
        ' ',
        lemmatized,
        flags=re.IGNORECASE
    )

    # Step 5: Normalize whitespace
    lemmatized = re.sub(
        r'\s+',
        ' ',
        lemmatized
    ).strip()

    return lemmatized
