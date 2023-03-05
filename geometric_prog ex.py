#----request a1,a2 and loop range

s1 = int(input("s1:")) #a1
s2 = int(input("s2:")) #a2
rseq = int(input("number of sequences to be printed:"))

x = s1
y = s2

#----common.ratio

cr = s2 / s1
cr = int(cr) #float to int

print("a1 =", s2,"/",s1)
print("with common.ratio =",cr)

for i in range(1,rseq+1):
    x = x * cr
    y = y * cr
    print(y,"/",x,)
