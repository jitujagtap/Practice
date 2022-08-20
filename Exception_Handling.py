
while True:
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter Second Number : "))

    try:
        result = num1/num2
        print("Result is : ", result)
    except:
        print("Number is not divisible by Zero, Please enter valid number")
