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
        except Exception as e:
            print(e)
    else:
        return "Error: Invalid operator"


expression = input("Enter an expression: ")
var = eval(expression)
print(var)
