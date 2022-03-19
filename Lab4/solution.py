
def getWords(filename):
  fname="/content/"+filename;
  file=open(fname,"r")
  content=file.read()
  content=content.lower()
  return content



print(getWords("file1.txt"))
print(getWords("file2.txt"))
print(getWords("file3.txt"))
print(getWords("file4.txt"))
