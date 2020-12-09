


import PyPDF2 as pdf
import pandas as pd
import re
import nltk

import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from click._compat import raw_input
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')
import nltk

data=open('top-100-places-to-visit-in-india.txt','r')
data

new_data=[]

for line in data:
  new_data.append(line)
  print(line,end=" ")

new_data

new_data=" ".join(new_data)
new_data

raw=new_data.lower()
raw=raw.replace('\\','')
raw=raw.replace('\n','')

raw = re.sub(r'\d+', '', raw)
raw = re.sub(' +', ' ',raw);

raw

import nltk
import numpy as np
import random
import string 
import re
nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ['hi', 'hey', '*nods*', 'hi there', 'hello', 'I am glad! You are talking to me']
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+'I am sorry! I do not understand you'
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
