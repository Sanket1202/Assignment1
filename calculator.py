def calculate(operand1, operator, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '%':
        return operand1 % operand2
    elif operator == '/':
        try:
            return operand1 / operand2
        except:
            print("Error: Division by zero is not possible")
    else:
        return "Error: Invalid operator"

expression = input("Enter an expression: ")
ls = expression.split(" ")
print(ls)
if len(ls) != 3:
    print("Error: Invalid expression")
else:
    operand1 = float(ls[0])
    operand2 = float(ls[2])
    operator = ls[1]
    result = calculate(operand1, operator, operand2)
    print("Result:", result)
