from cmath import log
import math
def sum():
    print("entre two number: ")
    n1=int(input())
    n2=int(input())
    print("sum: ",n1 + n2)

def sub():
    print("entre two number: ")
    n1=int(input())
    n2=int(input())
    print("sum: ",n1 - n2)

def mul():
    print("entre two number: ")
    n1=int(input())
    n2=int(input())
    print("sum: ",n1 * n2)

def div():
    try:
        print("entre two number: ")
        n1=int(input())
        n2=int(input()) 
        print("sum: ",n1 / n2)
    except ZeroDivisionError:
        print(" can not divide by zero")
    

def pow():
    print("number one is not the power number two ie")
    print("entre two number: ")
    n1=int(input())
    n2=int(input())
    print("sum: ",pow(n1,n2))

def rest_of():
    print("entre two number: ")
    n1=int(input())
    n2=int(input())
    print("sum: ",n1 % n2)

def dec_mul():
    print("number one is not the power number two ie")
    print("entre two number: ")
    n1=int(input())
   # n2=int(input())
    n2=1
    for i in range(n1,1,-1):
        n2=n2*i

    print("sum: ",n2)

def sin():
    print("entre a type of angle you need (rad,deg)")
    op=input()
    if(op=='rad'):
        print("entre number: ")
        n1=int(input()) 
        print("sum: ",math.sin(n1))
    elif(op=='deg'):
        print("entre number: ")
        n1=int(input()) 
        print("sum: ",math.sin(n1*(math.pi/180)))

def cos():
    print("entre a type of angle you need (rad,deg)")
    op=input()
    if(op=='rad'):
        print("entre number: ")
        n1=int(input()) 
        print("sum: ",math.cos(n1))
    elif(op=='deg'):
        print("entre number: ")
        n1=int(input()) 
        print("sum: ",math.cos(n1*(math.pi/180)))

def tan():
    print("entre a type of angle you need (rad,deg)")
    op=input()
    if(op=='rad'):
        print("entre number: ")
        n1=int(input()) 
        print("sum: ",math.tan(n1))
    elif(op=='deg'):
        print("entre number: ")
        n1=int(input()) 
        print("sum: ",math.tan(n1*(math.pi/180)))

def OR():
    print("entre two number: ")
    n1=int(input())
    n2=int(input())
    print("sum: ",n1 | n2)
def AND():
    print("entre two number: ")
    n1=int(input())
    n2=int(input())
    print("sum: ",n1 & n2)
def NOT():    
    print("entre number: ")
    n1=int(input())    
    print("sum: ", ~ n1)

while(1):
    print("entre operation you need to do (+,*,-,/,!,%,**(power),or,and,not,sin,cos,tan)")
    x=input()
    if(x=='+'):
       sum()
    elif(x=='-'):
       sub()
    elif(x=='*'):
        mul()  
    elif(x=='/'):
       div()
    elif(x=='**'):
       pow()   
    elif(x=='%'):
       rest_of() 
    elif(x=='!'):
        dec_mul() 
    elif(x=='and'):
        AND()
    elif(x=='or'):
        OR()
    elif(x=='not'):
        NOT()
    elif(x=='sin' or x=='SIN'):
        sin()  
    elif(x=='cos' or x=='COS'):
        cos()
    elif(x=='tan' or x=='TAN'):
        tan()
    else:
        print("error operation")
