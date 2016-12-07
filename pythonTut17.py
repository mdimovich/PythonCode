# Python Tutorial: Lecture 5
# December 6, 2016
# Insert an equation that includes a variable x to add/subtract, and solve for x


def solve_equation(equation):
    x, operator, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    if operator == "+":
        return "x = " + str(num2 - num1)
    elif operator == "-":
        return "x = " + str(num2+num1)


eq = input("Enter equation: ")
print(solve_equation(eq))



