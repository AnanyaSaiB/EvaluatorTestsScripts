import pickle as pkl
#import string
#from nltk.corpus import stopwords
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from mk_pkl_twit import preprocess

def get_con_chunks(text):
  chunked = ne_chunk(pos_tag(word_tokenize(text)))
  p = None
  con_chunk = []
  cur_chunk = []
  for i in chunked:
    if type(i) == Tree:
      cur_chunk.append(" ".join([tok for tok, pos in i.leaves()]))
    elif cur_chunk:
      ne = " ".join(cur_chunk)
      if ne not in con_chunk:
        con_chunk.append(ne)
        cur_chunk = []
    else:
      continue
  return con_chunk

x=[]
filen = 'response.txt'
#sp = "<first_speaker> "
sp = "<second_speaker> "

with open(filen) as f:
  for l in f:
    l = preprocess(l.decode('utf-8'))
    t = l.strip() #.translate(string.maketrans("",""),string.punctuation)
    stop = get_con_chunks(t) 
    wor = word_tokenize(t)
    fil_sen = [w for w in wor if not w in stop]
    out = " ".join(i for i in fil_sen)
    x.append("</s> " + sp + out + " </s>")
print x
with open(filen+'_no_ne.pkl','wb') as f:
  pkl.dump(x,f)
