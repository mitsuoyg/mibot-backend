from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
import re
import random


class Chatbot:

    def __init__(self):
        self.vectorizer = None
        self.knowledge = []

    def train(self, knowledge):
        self.knowledge = knowledge
        questions_hash = [self._semhash(q)
                          for k in knowledge for q in k['questions']]
        # vectorizer = TfidfVectorizer(token_pattern='[#a-zñ0-9]+')
        self.vectorizer = CountVectorizer(token_pattern='[#a-zñ0-9]+')
        self.vectorizer.fit(questions_hash)

    def getResponse(self, message):
        if not self.vectorizer:
            return

        questions, intentions = list(
            zip(*[[q, str(k['id'])] for k in self.knowledge for q in k['questions']]))
        sim = [self._similarity(message, q, self.vectorizer)
               for q in questions]
        idx = np.argmax(sim)
        k = next(k for k in self.knowledge if str(k['id']) == intentions[idx])

        return {
            'knowledge': k,
            'answer': random.choice(k['answers']),
            'score': sim[idx]
        }

    def _similarity(self, text1, text2, vectorizer):
        v1 = vectorizer.transform([self._semhash(text1)]).toarray()[0]
        v2 = vectorizer.transform([self._semhash(text2)]).toarray()[0]
        aux = np.linalg.norm(v1)*np.linalg.norm(v2)
        return 0 if aux == 0 else np.dot(v1, v2)/aux

    def _semhash(self, text):
        tokens = []
        text = self._clean(text)
        for t in text.split():
            if(t[0] != '@'):
                t = '#{}#'.format(t)
                tokens += self._ngrams(t)
        return ' '.join(tokens)

    def _clean(self, text):
        text = text.lower()
        text = re.sub(r'[^@_a-zá-úñÑ0-9\s]+', '', text)
        text = text.replace('á', 'a').replace('é', 'e').replace(
            'í', 'i').replace('ó', 'o').replace('ú', 'u')
        text = text.split()
        return ' '.join(text)

    def _ngrams(self, text, n=3):
        ngrams = zip(*[text[i:] for i in range(n)])
        ngrams = [''.join(ng) for ng in ngrams]
        return ngrams
