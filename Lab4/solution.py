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
  words=[]
  for x in content:
    if (removeNumeralWords(x)==True):
      purified = givePureEnglish(x)
      words.append(purified)

  return words



content1 = getWords("file1.txt")

content2 = getWords("file2.txt")
content3 = getWords("file3.txt")
content4 = getWords("file4.txt")
