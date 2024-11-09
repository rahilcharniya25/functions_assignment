#calculator app
numbers = []
number1 = int(input("enter the number you wanna perform operation on: "))
numbers.append(number1)
number2 = int(input("enter the number you wanna perform operation on: "))
numbers.append(number2)



def addition():
    global numbers
    total = numbers[0] + numbers[1]
    
    print(f"the sum of number is {total}")
    
def substraction():
    global numbers 
    if numbers[0]>numbers[1]:
        total = numbers[0] - numbers[1]
    else :
        print("please enter the valid number ")

    
    print(f"the substraction of number is {total}")

def division():

    global numbers
    
    if numbers[1] == 0:
        print("please enter the valid number ")
    else :
         total = numbers[0] / numbers[1]

    print(f"the division of number is {total}")

def multiplication():
    global numbers
    total = numbers[0] * numbers[1]
    print(f"the multiplication of number is {total}")

while True:
    print(" 1 if you wanna add two numbers ")
    print(" 2 if u wanna substract 2 number ")
    print(" 3 if you wanna divide two numbers ")
    print(" 4 if uou wanna multiply two numbers")
    print(" 5 to exit ")

    choice = input("enter your choice ")
    if choice =="1":
        addition()
    elif choice=="2":
        substraction()
    elif choice=="3":
        division()
    elif choice=="4":
        multiplication()
    elif choice=="5":
        break 
    else:
        print("please select correct choice ")



    
