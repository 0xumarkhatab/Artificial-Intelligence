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
