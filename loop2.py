'''for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()
------------------------
for i in range(1,5):
    for j in range(5,i,-1):
        print("*",end="")
    print()
--------------------
for i in range(1,5):
    for j in range(1,4):
        print('*',end='')
print(ord('A'))
print(chr(97))
---------------------
i=1
while i<=10:
    print(i,end=' ')
    i=i+1
----------------------
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()
O/P:
1
12
123
1234
----------------------
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end="")
    print()
O/P:
*
**
***
****
---------------------------
'''
for i in range(1,5):
    for j in range(5,i,-1):
        print("*",end="")
    print()

for i in range(1,5):
    for j in range(1,i,+1):
        print('*',end="")
    print()
