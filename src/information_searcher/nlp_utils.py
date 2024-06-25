import nltk

class NLPUtils:
    def text_classification(self, text):
        # Perform text classification using NLTK library
        classified_text = nltk.classify(text)
        return classified_text

    def entity_recognition(self, text):
        # Perform entity recognition using NLTK library
        entities = nltk.entity_recognize(text)
        return entities