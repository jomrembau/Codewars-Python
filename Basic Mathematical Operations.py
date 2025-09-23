


def basic_op(operator, value1, value2):
    if operator == "+":
        answer = value1 + value2
    elif operator == "-":
        answer = value1 - value2
    elif operator == "*":
        answer = value1 * value2
    elif operator == "/":
        answer = value1 / value2
    else:
        return "Enter Valid Operator"
    return answer



print(basic_op("*",2,4))