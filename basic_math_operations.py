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
        print("Oops!  That was no valid number.  Try again...")
        

    print("For addition select 1\nFor subtraction select 2\n \
        For multiplication select 3\n For division select 4")  # formatting should be improved
        
    while True:
        operator_value = input("Enter the value of your desired operation: ")
        if operator_value not in ['1', '2', '3', '4']:
            print("You have entered invalid input. Try again")
        else:
            break

    def addition(a,b):
        return a+b 
    def substraction(a,b):
        return a-b               
    def multiplication(a,b):
        return a*b
    def division(a, b):
        return a / b

    match operator_value:
        case '1':
            output = addition(value_1, value_2)
            print('Addition :: {} + {} = {}'.format(value_1, value_2, output))
        case '2':
            output = substraction(value_1, value_2)
            print('substraction :: {} - {} = {}'.format(value_1, value_2, output))
        case '3':
            output = multiplication(value_1, value_2)
            print('multiplication :: {} * {} = {}'.format(value_1, value_2, output))
        case '4':
            if value_2 == 0:
                print("The value of divident cannot be zero")
                continue
            output = division(value_1, value_2)
            print('division :: {} / {} = {}'.format(value_1, value_2, output))

    exit_value = input("Do you want to exit the program y/n: ")
    if exit_value in ['y','Y']:
        break

