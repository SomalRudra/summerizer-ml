
from transformers import T5ForConditionalGeneration, T5Tokenizer
import pickle

def loadAndDumpModel():
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    pickle.dump(model,open("model.pkl",'wb'))

def dumpTokenizer():
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    pickle.dump(tokenizer,open("tockenizer.pkl",'wb'))

loadAndDumpModel()
dumpTokenizer()