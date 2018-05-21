import pickle as pkl
import string
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
    t3 = word_tokenize(t)
    m = len(t2)
    done = []
    for i in range(m/2):
      y=random.randint(0,m-1)
      if y not in done:
        done.append(y)
    for j in done:
      t2[j] = t3[j]+" "+t3[j]
    out = " ".join(d for d in t2)
    x.append("</s> " + sp + out + " </s>")
print x
with open(filen+'_rep_words.pkl','wb') as f:
  pkl.dump(x,f)
