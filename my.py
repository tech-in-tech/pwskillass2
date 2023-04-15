# Q1 How can we store a single quote (‘) as a string in a variable?
name = "anubhav'Sharma"

# Q2 Refer the below var1able:
# x = 'a'
# Here, is x a character type or string type variable? Support your answer with an explanation.

'''Here a is string because it is between single quotes
'''


# Q3 Apply the follow1ng functions on this variable: Welcome to Python foundaton course
# 1 = find()
# 2 = count()
# 3 = len()
# 4 = concatination()
# Note: You can use your choice of parameters. But make sure it is correct.

variable1 = "Welcome to Python foundaton course"
variable2 = "Pw skills"
print(variable1.find('a'))
print(variable1.count('a'))
print(len(variable1))
variable3 = variable1+variable2
print(variable3)

word = "PanaJi@12256"
countlower = 0
for i in word:
    if i.islower():
        countlower+=1
print(countlower)
    
countupper = 0
for i in word:
    if i.isupper():
        countupper+=1

print(countupper)
    


countdigit = 0
for i in word:
    if i.isdigit():
        countdigit+=1

print(countdigit)


# code to store a numerical value and convert it into string
num = int(input("number : "))
num = str(num)
print(type(num))