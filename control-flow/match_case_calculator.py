num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
opera=input("Choose the operation (+, -, *, /): ")
match opera:
    case "+":
        add = num1 + num2
        print(f"The result is {add}.")
    case "-":
        sub = num1 - num2
        print(f"The result is {sub}.")
    case "*":
        mul = num1 * num2
        print(f"The result is {mul}.")
    case "/":
        if num2!=0:
            divi = num1 / num2
            print(f"The result is {divi}.")
        else:
            print("Cannot divide by zero.")