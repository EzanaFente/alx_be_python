num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
opera=input("Choose the operation (+, -, *, /): ")
match opera:
    case "+":
        result = num1 + num2
        print(f"The result is {int(result)}.")
    case "-":
        result = num1 - num2
        print(f"The result is {int(result)}.")
    case "*":
        result = num1 * num2
        print(f"The result is {int(result)}.")
    case "/":
        if num2!=0:
            result = num1 / num2
            print(f"The result is {int(result)}.")
        else:
            print("Cannot divide by zero.")