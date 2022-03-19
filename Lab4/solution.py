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
    print('',self.word,'\t\t',self.count,'\t',self.probability)



def printWord(word):
  word.print()

def printWords(words):
  print(f'\n\t\t--Probabilties--\n')
  print(f'Word\t\tCount\t Probabilty\n')
  for x in words:
    printWord(x)
  


def countProbability(words,probabilities):
  nonduplicated=set(words) # removing duplicates
  length=len(words)
  for x in nonduplicated:
    wordCount=words.count(x)  
    element=wordProbability(x,wordCount,length)
    #element.print()
    probabilities.append(element)

  return probabilities

content1 = getWords("file1.txt")
content2 = getWords("file2.txt")
content3 = getWords("file3.txt")
content4 = getWords("file4.txt")
probabilities=deque()
probabilities = countProbability(content1,probabilities)
probabilities =  countProbability(content2,probabilities)
probabilities =  countProbability(content3,probabilities)
probabilities =  countProbability(content4,probabilities)

printWords(probabilities)





# Question 2
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
        
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())

