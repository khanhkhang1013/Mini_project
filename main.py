import sys
def add(a,b):
return a+b
if __name__=="main__:
a,b = sys.argv[1], sys.argv[2] # python execute param1
print(a, b)
print(add(a, b))
print(sub(a, b))
