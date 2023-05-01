import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarizer(rawdoc):
    # Defining Stop-Words:
    stopwords = list(STOP_WORDS)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(rawdoc)

    # Tokenization:
    tokens = [token.text for token in doc]
    
    # Word Frequency:
    word_freq = {}

    for word in doc:
        # If token is NOT a stopword and is NOT a punctuation:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            # If the word is NOT already present in the "word_freq" Dictionary, add it:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            # If word is present in the "word_freq" Dictionary, increase its frequency by 1:
            else:
                word_freq[word.text] += 1

    # Maximum Frequency:
    max_freq = max(word_freq.values())
    
    # Normalization of Frequencies:
    for word in word_freq.keys():
        word_freq[word] = word_freq[word] / max_freq

    # Creating tokens of Sentences:
    sent_tokens = [sent for sent in doc.sents]

    # Calculating Sentence Score, which is the sum of Normalized Frequencies of
    # all the tokens occuring in the sentence:

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]


    # Defining the Length of the Summary to be Created:

    summaryLength = int(len(sent_tokens) * 0.3)
    summary = nlargest(summaryLength, sent_scores, key=sent_scores.get)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    return summary, doc, len(rawdoc.split(' ')), len(summary.split(' '))
