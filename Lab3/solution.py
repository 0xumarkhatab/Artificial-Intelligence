# Umar Khatab
# 19L-2765
# Section B
# Lab3 
# Question 1
def symmetric_difference(a,b):
  return a.symmetric_difference(b)
symmetric_difference({1,2,3},{3,4,5})

# Questoin 2
def divide(p,q):
  try:
    return p/q
  except ZeroDivisionError:
    print(f"Division by Zero Error")
divide(1,0)
divide(1,2)

# Question 3

# in open Command , specify the path of the file to work on,
# in my case , it is /content.file.txt and im opening it for reading purpose

file = open("/content/file.txt","r")

# reading all the file 
data =file.read();

length=len(data);

print("length is ",length)

index=0
# python built in function 
def reverse(message):
  return message[::-1]
reversed=reverse(data)
print(reversed)
file.close()

file = open("/content/reversed.txt","w")
file.write(reversed)
file.close()


