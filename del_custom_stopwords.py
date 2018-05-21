import pickle as pkl
#import string
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
x=[]
filen = 'twit_res'
#sp = "<first_speaker> "
sp = "<second_speaker> "

with open("response.txt.pkl",'rb') as fi:
  f = pkl.load(fi)
for l in f:
    t = l.strip() #.translate(string.maketrans("",""),string.punctuation)
    #stop = set(stopwords.words('english'))
    stopwords = ['a','an','and','are','as','at','be','by','for','from','has','he','in','is','it','its','of','on','that','the','to','was','were','will','with']
    stop = set(stopwords)
    wor = word_tokenize(t)
    fil_sen = [w for w in wor if not w in stop]
    out = " ".join(i for i in fil_sen)
    x.append(out)
    #x.append("</s> " + sp + out + " </s>")
print x
with open(filen+'_no_stopwords_custom.pkl','wb') as f:
  pkl.dump(x,f)
