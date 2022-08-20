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
print("My City "+" Pune")
print("My City "+" Haiderbad!!!",end='')
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
a=236
b=a%10 #3
c=int(a/10)# 12
d=c%10 # 2
e=int(c/10)
f=b*100+d*10+e
print(f)
name='lotus'
print(name[::-1])
import sys; x = 'foo'; sys.stdout.write(x + '\n')

str = 'Suryansh'
print (str)         # Prints complete string
print (str[0])      # Prints first character of the string
print (str[2:5])    # Prints characters starting from 3rd to 5th
print (str[2:])     # Prints string starting from 3rd character
print (str * 2)     # Prints string two times
print (str + "Jagtap")  # Prints concatenated string

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list)
print (list[0])
print (list[2:3])
print (list[1])
print (tinylist * 2)
print (list + tinylist)

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)               # Prints the complete tuple
print(tuple[0])            # Prints first element of the tuple
print(tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd
print(tuple[2:])           # Prints elements of the tuple starting from 3rd element
print(tinytuple * 2)       # Prints the contents of the tuple twice
print(tuple + tinytuple)   # Prints concatenated tuples

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

