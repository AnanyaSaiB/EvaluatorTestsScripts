import pickle as pkl
#import string
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from mk_pkl_twit import preprocess

x=[]
filen = 'response.txt'
#sp = "<first_speaker> "
sp = "<second_speaker> "

with open(filen) as f:
  for l in f:
    l = preprocess(l.decode('utf-8'))
    t = l.strip() #.translate(string.maketrans("",""),string.punctuation)
    nouns = []
    #nouns_n_verbs = []
    for w,pos in nltk.pos_tag(nltk.word_tokenize(t)):
      if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(w)
    out = " ".join(i for i in nouns)
    x.append("</s> " + sp + out + " </s>")
print x
with open(filen+'_nouns.pkl','wb') as f:
  pkl.dump(x,f)
