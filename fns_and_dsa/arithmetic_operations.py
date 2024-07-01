def perform_operation(num1,num2,operation):
    num1=float(num1)
    num2=float(num2)
    operation=str(operation)

    match operation:
     case "add":
        result = num1 + num2
        print(f"Result: {result}")
     case "subtract":
        result = num1 - num2
        print(f"Result: {result}")
     case "multiply":
        result = num1 * num2
        print(f"Result: {result}")
     case "divide":
        if num2!=0:
            result = num1 / num2
            print(f"Result: {result}")
        else:
            print("Cannot divide by zero.")
            
# num1=float(input("Enter the first number: "))
# num2=float(input("Enter the second number: "))
# operation=str(input("Enter the operation (add, subtract, multiply, divide): "))
#perform_operation(num1,num2,operation)