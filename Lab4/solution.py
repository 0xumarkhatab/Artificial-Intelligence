# Question 1
import re

def isAccepted(string):
 
    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[0123456789@_!#$%^&*()<>?/\|}{~:]')
     
    # Pass the string in search
    # method of regex object.   
    if(regex.search(string) == None):
        return True
         
    else:
        return False
   
def getWords(filename):
  fname="/content/"+filename;
  file=open(fname,"r")
  content=file.read()
  content=content.lower()
  content= content.split(sep=' ') # separating words
  return content



print(getWords("file1.txt"))
print(getWords("file2.txt"))
print(getWords("file3.txt"))
print(getWords("file4.txt"))
