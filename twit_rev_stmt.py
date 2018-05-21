import pickle as pkl
#import string
import random
from nltk.tokenize import word_tokenize
from mk_pkl_twit import preprocess
x=[]
filen = 'response.txt'
#sp = "<first_speaker> "
sp = "<second_speaker> "

with open(filen) as f:
  for l in f:
    l = preprocess(l.decode('utf-8'))
    t = l.strip()#.translate(string.maketrans("",""),string.punctuation)
    #m = len(t)
    t2 = word_tokenize(t) #t.split(" ")
    #random.shuffle(t2)
    t2 = t2[-1::-1]
    out = " ".join(t2)
    x.append("</s> " + sp + out + " </s>")
print x
with open(filen+'_rev_sent.pkl','wb') as f:
  pkl.dump(x,f)
