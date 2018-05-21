import pickle as pkl
#import string
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from mk_pkl_twit import preprocess
import nltk

x=[]
filen = 'response.txt'
#sp = "<first_speaker> "
sp = "<second_speaker> "

with open(filen) as f:
  for l in f:
    l = preprocess(l.decode('utf-8'))
    t = l.strip() #.translate(string.maketrans("",""),string.punctuation)
    pro_nouns_vs = []
    #nouns_n_verbs = []
    for w,pos in nltk.pos_tag(nltk.word_tokenize(t)):
      if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS' or pos == 'PRP' or pos == 'PSP$' or pos == 'VB'or pos == 'VBD'or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ'):
             pro_nouns_vs.append(w)
    out = " ".join(i for i in pro_nouns_vs)
    x.append("</s> " + sp + out + " </s>")
print x
with open(filen+'_simp_sent_nouns_pro_verbs.pkl','wb') as f:
  pkl.dump(x,f)
