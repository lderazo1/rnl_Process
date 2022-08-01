import spacy
from stanza.models.common.doc import Document
from stanza.pipeline.core import Pipeline
from cache_ import *

def evaluate_language(message):
    nlp = Pipeline(lang="multilingual", processors="langid")
    docs = message.split('.')
    docs = [Document([], text=text) for text in docs]
    docs = nlp(docs)
    print("\n".join(f"{doc.text}\t{doc.lang}" for doc in docs))
    return docs

def get_information(message):
    message = evaluate_structure(message)
    nlp = spacy.blank("en")
    nlp.add_pipe('opentapioca')
    doc = nlp(message)
    return(doc.ents)