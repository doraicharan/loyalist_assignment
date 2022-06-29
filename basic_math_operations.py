while True:
    print("Program to calculate basic math operations")

    value_1 = input("Enter the first value: ")  # Should add error handling here

    value_2 = input("Enter the Second value: ")  # Should add error handling here

    print("For addition select 1\n For subtraction select 2\n \
        For multiplication select 3\n For division select 4")
        
    while True:
        operator_value = input("Enter the value of your desired operation: ")
        if operator_value not in ['1', '2', '3', '4']:
            print("You have entered invalid input. Try again")
    
    match operator_value:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

    exit_value = input("Do you want to exit the program y/n: ")
    if exit_value in ['y','Y']:
        break

