import pickle as pkl
#import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from mk_pkl_twit import preprocess
x=[]
filen = 'response.txt'
#sp = "<first_speaker> "
sp = "<second_speaker> "

with open(filen) as f:
  for l in f:
    l = preprocess(l.decode('utf-8'))
    t = l.strip() #.translate(string.maketrans("",""),string.punctuation)
    stop = set(stopwords.words('english'))
    wor = word_tokenize(t)
    fil_sen = [w for w in wor if not w in stop]
    out = " ".join(i for i in fil_sen)
    x.append("</s> " + sp + out + " </s>")
print x
with open(filen+'_no_stopwords.pkl','wb') as f:
  pkl.dump(x,f)
