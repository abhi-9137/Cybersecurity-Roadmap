
a=int(input("A=>"))
b=int(input("B=>"))
c=int(input("C=>"))

if(a>=b and b>=c):
    print("a is the greatest",a)
elif(b>=a and a>=c):
    print("b is the greatest",b)

else: 
    print("c is the greatest",c)   
