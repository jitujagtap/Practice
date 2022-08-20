print('Hello World!!')
print("Hello World!!!")
print('''Hello World!!''')
a=1000
b=123.45
c='A'
d="abhiraj"
print(a,b,c,d)
print(a," ",b)
name='Raju'
print(name+"My City "+" Pune")
print("My City "+" Hydrabad!!!",end='') #end='' is used to continue the next print immediately after the Hyderabad
a,b,c,d,e=12,'A',"Lotus",True,34.67
print(a,b,c,d,e,sep=',')
n1,n2,n3=100,200,300
print('{} {} {}'.format(n1,n2,n3))
print(' %d %c %s  %g %f '%(a,b,c,d,e))
a,b=1000,20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(int(a/b))
a=123
b=a%10 #3
c=int(a/10)# 12
d=c%10 # 2
e=int(c/10)
f=b*100+d*10+e
print(f)
name='lotus'
print(name[::-1])

a=200
b=100
c=500
if(a>=b) and (a>=c):
    print("a is grater")
elif(b>=a) and (b>=c):
    print("b is grater")
else:
    print("c is grater")

