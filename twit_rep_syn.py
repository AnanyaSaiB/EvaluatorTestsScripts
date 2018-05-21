import pickle as pkl
#import string
#from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from random import randint
from mk_pkl_twit import preprocess

# Load a text file if required
#text = "Pete ate a large cake. Sam has a big mouth."
#output = ""

# Load the pretrained neural net
#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Tokenize the text
#tokenized = tokenizer.tokenize(text)

def replace_syn(text):
 output = ""
 # Get the list of words from the entire text
 words = word_tokenize(text)

 # Identify the parts of speech
 tagged = pos_tag(words)

 for i in range(0,len(words)):
    replacements = []

    if len(words[i]) <= 3:
        output = output + " " + words[i]
        continue

    # Only replace nouns with nouns, vowels with vowels etc.
    for syn in wordnet.synsets(words[i]):

        # Do not attempt to replace proper nouns or determiners
        if tagged[i][1] == 'NNP' or tagged[i][1] == 'DT':
            break
        
        # The tokenizer returns strings like NNP, VBP etc
        # but the wordnet synonyms has tags like .n.
        # So we extract the first character from NNP ie n
        # then we check if the dictionary word has a .n. or not 
        word_type = tagged[i][1][0].lower()
        if syn.name().find("."+word_type+"."):
            # extract the word only
            r = syn.name()[0:syn.name().find(".")]
            replacements.append(r)

    if len(replacements) > 0:
        # Choose a random replacement
        replacement = replacements[randint(0,len(replacements)-1)]
        output = output + " " + replacement.encode("ascii")
    else:
        # If no replacement could be found, then just use the
        # original word
        output = output + " " + words[i]

 return output

x=[]
filen = 'response.txt'
#sp = "<first_speaker> "
sp = "<second_speaker> "

with open(filen) as f:
  for l in f:
    l = preprocess(l.decode('utf-8'))
    t = l.strip() #.translate(string.maketrans("",""),string.punctuation)
    #stop = get_con_chunks(t) 
    #wor = word_tokenize(t)
    #fil_sen = [w for w in wor if not w in stop]
    out = replace_syn(t) #" ".join(i for i in fil_sen)
    x.append("</s> " + sp + out + " </s>")
print x
with open(filen+'_replace_syn.pkl','wb') as f:
  pkl.dump(x,f)
