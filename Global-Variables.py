x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "Greatest"

myfunc()

print("Python is " + x)