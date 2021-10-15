a=float(input("Enter 1st number"))
b=float(input("Enter 2nd number"))

def divide(a,b):
    result=a/b
    print(result)

def multiply(a,b):
    result=a*b
    print(result)

def sum(a,b):
    result=a+b
    print(result)

def subtract(a,b):
    result=a-b  
    print(result) 

print("Select operation.")
print("1.sum")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
op =int(input("Enter the operator"))
if op ==1:
    sum(a,b)
elif op ==2:
    subtract(a,b)
elif op ==3:
    multiply(a,b)
elif op ==4:
    divide(a,b)
else:
    print("invalid")

    





