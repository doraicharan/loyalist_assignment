while True:
    print("Program to calculate basic math operations")

    while True:
     try:
         value_1 = int(input("Enter the first value: "))
         break
     except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    while True:
     try:
         value_2 = int(input("Enter the Second value: "))
         break
     except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    print("For addition select 1\n For subtraction select 2\n \
        For multiplication select 3\n For division select 4")
        
    while True:
        operator_value = input("Enter the value of your desired operation: ")
        if operator_value not in ['1', '2', '3', '4']:
            print("You have entered invalid input. Try again")

    def addition(a,b):
        return a+b        
    
    match operator_value:
        case 1:
            output = addition(value_1, value_2)
            print('Addition :: {} + {} = {}'.format(value_1, value_2, output))
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

    exit_value = input("Do you want to exit the program y/n: ")
    if exit_value in ['y','Y']:
        break

