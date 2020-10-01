
def test():
    print('Im a function')

def separator():
    print("-------------")


print ('Hello Python')

#variables
name ='Mesaye'
last ='Addisu'
age = 35
found = False
total = 23.43
products = []

print(name)
print(name + " " + last)

print(name + str(age))

separator()

#math operation
print (age -10)
print (age + 10)
print (age * 2)
print (age / 2)
print(age % 2) # mod operator

separator()

# if statement
if(age < 80):
    print('You are still young!')
    print('something else')
elif(age == 80):
    print('you are on the border line')    
else:
    print('sorry, you are getting old :|')    