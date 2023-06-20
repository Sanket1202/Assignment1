def calculate(exp):
    try:
        var = eval(exp)
        return var
    except Exception as e:
        return e

expression = input("Enter the expression:")
result = calculate(expression)
print("Result is:", result)
