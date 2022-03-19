# Question 1
import re
from collections import deque

def removeNumeralWords(string):
 
    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[0123456789@_!#$%^&*()<>?/\|}{~:]')
     
    # Pass the string in search
    # method of regex object.   
    if(regex.search(string) == None):
        return True
         
    else:
        return False
def givePureEnglish(string):
      regex = re.compile('[a-zA-Z]')
      newStr=""
      for x in string:
        if(regex.search(x) !=None ):
          newStr+=x
        
      return newStr


def getWords(filename):
  fname="/content/"+filename;
  file=open(fname,"r")
  content=file.read()
  content=content.lower()
  content= content.split(sep=' ') # separating words
  words=deque()
  for x in content:
    if (removeNumeralWords(x)==True):
      purified = givePureEnglish(x)
      words.append(purified)

  return words



class wordProbability:
  "This Class Stores The Word , Count and It's Probabilty "
  word=None
  count=-1
  probability=-1
  def __init__(self, w, c,p):
    self.word=w
    self.count=c
    self.probability=p
  def print(self):
    print('',self.word,' ',self.count,' ',self.probability)




def countProbability(words):
  nonduplicated=set(content1) # removing duplicates
  length=len(words)
  probabilities=deque()
  for x in nonduplicated:
    wordCount=words.count(x)  
    eleProb=" "+str(wordCount)+"/"+str(length)
    element=wordProbability(x,wordCount,length)
    probabilities.append(element)

  return probabilities

content1 = getWords("file1.txt")
content2 = getWords("file2.txt")
content3 = getWords("file3.txt")
content4 = getWords("file4.txt")

for x in countProbability(content1):
  x.print()





