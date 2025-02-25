def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

result = calculate(int(input("Enter the first digit : ")), int(input("Enter the Second digit : ")), input('Enter the Operation to be perform : '))
print(result)
