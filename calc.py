
#functions
def print_menu():
    print("-"* 20)
    print(" python Calc")
    print("-"* 20)

    print("[1] add ")
    print("[2] subtract")
    print("[3] multiply")
    print('[4] Division')

    print("[5] My age")

    print('[x] Close')

"""
opc =5
ask for the year of birth
tell the age (+/- 1)
"""




    #instruction

opc = ''
while( opc!= 'x'):
    print_menu()
    opc = input('Please choose an option:')

    num1 = input("First number:")  
    num2 = input("Second number:")
    age =  input("Your Date of Birth")

    if(opc == '1'):
        
        res = float(num1) + float(num2)
        print("Result"+ (res))
    
    elif (opc == '2'):
        
        res = float(num1) - float(num2)
        print("Result"+ (res))  

    elif (opc == '3'):
    
        res = float(num1) * float(num2)
        print("Result"+ (res))  

    elif (opc == '4'):
        if(num2 == '0'):
            print("Don't divide by zero, y will kill us ALL")
        else:
            res = float(num1) / float(num2)
            print("Result"+ str(res))       
       
    elif (opc == '5'):
        res = (2020) - input
        print("Your age is"+ str(res))

print('Good bye!')