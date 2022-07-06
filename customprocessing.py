#import 
import pandas as pd
import pickle
import re
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences


def preprocess(text):
    """Do all the Preprocessing as shown above and
    return a tuple contain preprocess_email,preprocess_subject,preprocess_text for that Text_data"""
         
    
    #After you store it in the list, Replace those sentances in original text by space.
    text = re.sub("(Subject:).+"," ",text,re.I)
    
    #Delete all the sentances where sentence starts with "Write to:" or "From:".
    text = re.sub("((Write to:)|(From:)).+","",text,re.I)
    
    #Delete all the tags like "< anyword >"
    text = re.sub("<[^><]+>","",text)
    
    #Delete all the data which are present in the brackets.
    text = re.sub("\([^()]+\)","",text)
    
    #Remove all the newlines('\n'), tabs('\t'), "-", "".
    text = re.sub("[\n\t\\-]+","",text)
    
    #Remove all the words which ends with ":".
    text = re.sub("(\w+:)","",text)
    
    #Decontractions, replace words like below to full words.

    lines = re.sub(r"n\'t", " not", text)
    lines = re.sub(r"\'re", " are", lines)
    lines = re.sub(r"\'s", " is", lines)
    lines = re.sub(r"\'d", " would", lines)
    lines = re.sub(r"\'ll", " will", lines)
    lines = re.sub(r"\'t", " not", lines)
    lines = re.sub(r"\'ve", " have", lines)
    lines = re.sub(r"\'m", " am", lines)
    text = lines
    
        #replace numbers with spaces
    text = re.sub("\d+"," ",text)
    
        # remove _ from the words starting and/or ending with _
    text = re.sub("(\s_)|(_\s)"," ",text)
    
        #remove 1 or 2 letter word before _
    text = re.sub("\w{1,2}_","",text)
    
        #convert all letters to lowercase and remove the words which are greater 
        #than or equal to 15 or less than or equal to 2.
    text = text.lower()
    
    text =" ".join([i for i in text.split() if len(i)<15 and len(i)>2])
    
    #replace all letters except A-Z,a-z,_ with space
    preprocessed_text = re.sub("\W+"," ",text)

    return preprocessed_text

def preprocess_tokenizing(text):
        
    #from tf.keras.preprocessing.text import Tokenizer
    #from tf.keras.preprocessing.sequence import pad_sequences
    
    tokenizer = pickle.load(open('tokenizer.pkl','rb'))

    max_length = 1019
    tokenizer.fit_on_texts([text])
    encoded_docs = tokenizer.texts_to_sequences([text])
    text_padded = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
    
    return text_padded

import collections

def postprocess(vector):
    lookup =  {0: 'alt.atheism', \
      1: 'comp.graphics',\
      2: 'rec.sport.hockey',\
      3: 'sci.space',\
      4: 'talk.politics.misc'}

    d = dict(zip( lookup.values(),[ str(x) for x in vector] ))
    return d
    