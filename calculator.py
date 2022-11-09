import math

def add():  
    result = a + b
    print(result,"\n")

def sub():
    result = a - b
    print(result,"\n")

def mult():
    result = a * b
    print(result,"\n")

def div():
    result = a / b
    print(result,"\n")

def squareroot():
    result = math.sqrt(a)
    print(result,"\n")

op_dictionary = {'add':add,'sub':sub,"mult":mult,"div":div,"sqrt":squareroot}

while True:
    try:
        func_call = input("operator call")
        
        if func_call not in op_dictionary:
            print("Try Again")
            continue
        else:
            break
        
    except KeyError:
        print('Consider using a valid operator, \n => add, sub, mult, div')
        continue

while True:
    if func_call == "sqrt":   
        try:    
            a = int(input("X >"))
            op_dictionary[func_call]()
            break

        except ValueError:
            print("Try using integers or floats")
            continue

    else:
        try:
            a = int(input("x >"))
            b = int(input("Y >"))
            op_dictionary[func_call]()
            break

        except ValueError:
            print("Try using integers or floats")
            continue

# © Prince Santhosh/nmhappu