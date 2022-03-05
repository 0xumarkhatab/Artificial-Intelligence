# Task 1
def removeValue(sampleList, val):
  retValue =  [ num for num in sampleList if num!=val]
  return retValue
  pass
print(removeValue([1,2,3,2,23,4,1,2],2))
# LAB (end solution)

# Task 2
def findAndReplaceValue(sampleList, val):
  
  length = len(sampleList);
  counter=0;


  while counter<length:
    if(sampleList[counter]==val):
      sampleList[counter]=200
    counter=counter+1;
  pass
  return sampleList;  
  # LAB (end solution)
print(findAndReplaceValue([1,2,3,2,23,4,1,2],2 ))
