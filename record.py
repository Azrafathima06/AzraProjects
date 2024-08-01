import numpy as np
import nltk
nltk.download('omw-1.4')
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#Importing and reading the given information
GreetInputs = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
Greet_Responses = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad you are talking to me!"]
f=open("chatbot.txt","r",errors="ignore") 
raw_doc=f.read()
raw_doc=raw_doc.lower()#converting to lower texts for easier understanding
nltk.download('punkt')#using the punkt tokenizer
nltk.download("wordnet")#dictionary
sent_tokens=nltk.sent_tokenize(raw_doc) #Converts doc to a list of sentences
word_tokens=nltk.word_tokenize(raw_doc) #Converts doc to a list of words
print(sent_tokens[:2])
print(word_tokens[:2])
#Pre processing the texts
lemmer=nltk.stem.WordNetLemmatizer()
class talkBot:
  def LemTokens(self, tokens):
    return[lemmer.lemmatize(token) for token in tokens]  

  def LemNormalize(self,text):
    remove_punct_dict = dict((ord(punct),None) for  punct in string.punctuation)
    return self.LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
  
  def greet(self,sentence):
    for word in sentence.split():
      if word.lower() in GreetInputs:
        return random.choice(Greet_Responses)

  def response(self,user_response):
    robo1_response=" "
    TfidfVec=TfidfVectorizer(tokenizer=self.LemNormalize, stop_words="english")
    tfidf=TfidfVec.fit_transform(sent_tokens)
    vals=cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat=vals.flatten()
    flat.sort()
    req_tfidf=flat[-2]
    if(req_tfidf==0):
      robo1_response+="I am sorry, I don't understand you"
      return robo1_response
    else:
      robo1_response+=sent_tokens[idx]
      return robo1_response

  def start(self,userresp):
    flag=True
    print("BOT: My name is Stark. Let's have a conversation! Also, if you want to exit any time, just type Bye!")
    while(flag==True):
      #user_response=input()
      user_response=userresp
      user_response=user_response.lower()
      if(user_response!="bye"):
        if(user_response=="thanks" or user_response=="thank you"):
          flag=False
          print("BOT: You are welcome.")
          return "BOT: You are welcome."
        else:
          if(self.greet(user_response)!=None):
            print("BOT: "+ self.greet(user_response))
            return self.greet(user_response)
          else:
            sent_tokens.append(user_response)
            wordtokens=word_tokens+nltk.word_tokenize(user_response)
            final_words=list(set(wordtokens))
            print("BOT: ",end="")
            return self.response(user_response)
            #sent_tokens.remove(user_response)
      else:
        flag=False
        print("BOT: Goodbye! ")
        return "Goodbye! "
    