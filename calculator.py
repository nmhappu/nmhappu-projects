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

func_dict = {'add':add,'sub':sub,"mult":mult,"div":div}

a = int(input("X > "))
b = int(input("Y > "))

#print(a+b)

call_func = input("op > ")
func_dict[call_func]()
