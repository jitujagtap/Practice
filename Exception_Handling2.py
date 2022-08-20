x = 5.0
if type(x) is int:
    print("x is interger")
elif type(x) is float:
    print("x is float")
else:
    raise TypeError("Only integers are allowed")
