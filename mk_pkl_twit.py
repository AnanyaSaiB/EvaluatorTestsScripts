import pickle as pkl
import re
#import string
x=[]
filen = 'context.txt'
sp = "<first_speaker> "
#sp = "<second_speaker> "

def preprocess(s):
		while '@@ ' in s:
			s = s.replace('@@ ', '')

		utterance = s.replace('@user', '<at>').replace('&lt;unk&gt;', '<unk>').replace('&lt;heart&gt;', '<heart>').replace('&lt;number&gt;', '<number>').replace('  ', ' </s> ').replace('  ', ' ')
		# Make sure we end with </s> token
		utterance = utterance.replace('user', '<at>')
		#utterance = utterance.replace('A:', '<first_speaker>')
		#utterance = utterance.replace('B:', '<second_speaker>')
		utterance = utterance.replace('& lt', '<')
		utterance = utterance.replace('& gt', '>')
		utterance = utterance.replace('&lt;', '<')
		utterance = utterance.replace('&gt;', '>')
		utterance = utterance.replace('\'', ' \'')
		utterance = utterance.replace('"', ' " ')
		utterance = utterance.replace("'", " '")
		utterance = utterance.replace(";", " ")
		utterance = utterance.replace("`", " ")
		utterance = utterance.replace("..", ".")
		utterance = utterance.replace("..", ".")
		utterance = utterance.replace("..", ".")
		utterance = utterance.replace(",,", ",")
		utterance = utterance.replace(",,", ",")
		utterance = utterance.replace(",,", ",")
		utterance = utterance.replace('.', ' . ')
		utterance = utterance.replace('!', ' ! ')
		utterance = utterance.replace('?', ' ? ')
		utterance = utterance.replace(',', ' , ')
		utterance = utterance.replace('~', '')
		utterance = utterance.replace('-', ' - ')
		utterance = utterance.replace('*', ' * ')
		utterance = utterance.replace('(', ' ')
		utterance = utterance.replace(')', ' ')
		utterance = utterance.replace('[', ' ')
		utterance = utterance.replace(']', ' ')
		utterance = re.sub('[\s]+', ' ', utterance)
		utterance = utterance.replace('  ', ' ')
		utterance = utterance.replace('  ', ' ')
		s = utterance
		while '! ! ! !' in s:
		    s = s.replace('! ! ! !', '! ! !')
		#s = utterance.replace('/', ' ')
		#while s[-1] == ' ':
		#    s = s[0:-1]
		#if not s[-5:] == ' </s>':
		#    s = s + ' </s>'
		return unicode(s)

with open(filen) as f:
  for l in f:
    l = preprocess(l.decode('utf-8'))
    out = l.strip()#.translate(string.maketrans("",""),string.punctuation)
    x.append("</s> " + sp + out + " </s>")
print x
with open(filen+'.pkl','wb') as f:
  pkl.dump(x,f)
