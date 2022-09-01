import math

def add():  
    sum = a + b
    print(sum,"\n")

def sub():
    sub = a - b
    print(sub,"\n")

def mult():
    mult = a * b
    print(mult,"\n")

def div():
    div = a / b
    print(div,"\n")

def squareroot():
    rootof = math.sqrt(a)
    print(rootof,"\n")

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