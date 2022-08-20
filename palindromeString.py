#WAP to check if the entered string is Palindrome or not

str = input("Enter your string : ")

def palindrome(str):
    str1 = (str[: :-1])
    if str == str1:
        print("Entered String is Palindrome")
    else:
        print("Entered String is not palindrome")

palindrome(str)