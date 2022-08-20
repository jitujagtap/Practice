email = input ("Enter your email address : ")
atIndex = email.index("@")
username = email[0:atIndex]

domain = email[atIndex+1:]
dotIndex = domain.index(".")
company = domain[0:dotIndex]
print(username)
print(company)

#*********************************************************
name = input('Enter your name : ')
print(name)

age = int(input('Enter your age : '))
print(age)
print(type(age))

s = 'I am Jitendra.'
s1 = "I am learning Python."
s2 = """I am working with Unibeam."""
s3 = '''I love Pune.'''

print(s, s1, s2, s3, sep="\n")

