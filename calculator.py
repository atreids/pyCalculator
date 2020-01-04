
#This function adds 2 numbers
def add(cur_num, add_amount):
    cur_num += add_amount
    return cur_num

#This functions subtracts two numbers
def subtract(cur_num, sub_amount):
    cur_num -= sub_amount
    return cur_num

def multiple(cur_num, mul_amount):
    cur_num *= mul_amount
    return cur_num

def divide(cur_num, div_amount):
    cur_num /= div_amount
    return cur_num

def square(cur_num):
    cur_num **= 2
    return cur_num

def exit():
    print("Exiting...")
    return False
    
running = True

while running == True:
    print("""
    Please enter operation:
    1. Add
    2. Subtract
    3. Multiple
    4. Divide
    0. Exit
    """)
    operation = int(input("Entry:"))
    if operation == 0:
        running = exit()
        break
    num1 = float(input("Please enter number 1: "))
    num2 = float(input("Please enter number 2: "))

    if operation == 1:
        print(str(num1) + " + " + str(num2) + " = " + str(add(num1,num2)))
    elif operation == 2:
        print(str(num1) + " - " + str(num2) + " = " + str(subtract(num1,num2)))
    elif operation == 3:
        print(str(num1) + " * " + str(num2) + " = " + str(multiple(num1,num2)))
    elif operation == 4:
        print(str(num1) + " / " + str(num2) + " = " + str(divide(num1,num2)))
    else:
        print("Invalid input")









                    

    
