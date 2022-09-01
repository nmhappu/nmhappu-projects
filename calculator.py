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

op_dictionary = {'add':add,'sub':sub,"mult":mult,"div":div}

while True:
    try:
        a = float(input("X >"))
        b = float(input("Y >"))

    except ValueError:
        print('Try using integers or floats')
        continue

    break

while True:
    try:
        oper = input("Functions: \n add, sub, mult, by \n => ? ")
        op_dictionary[oper]()

    except KeyError:
        print("Try using a valid operator.")
        continue

    break
