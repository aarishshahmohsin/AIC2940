def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if is_empty(stack):
        return "Underflow"
    return stack.pop()


def peek(stack):
    if is_empty(stack):
        return "Underflow"
    return stack[-1]


def size(stack):
    return len(stack)


def is_operator(c):
    return c in "+-*/^"


def precedence(operator):
    if operator in {"+", "-"}:
        return 1
    if operator in {"*", "/"}:
        return 2
    if operator in {"^"}:
        return 3
    else:
        return 0


def infix_to_postfix(infix):
    postfix = ""
    stack = []
    stack.append("(")
    infix.append(")")

    for i in infix:
        if i == "(":
            push(stack, i)
        elif i == ")":
            while peek(stack) != "(":
                postfix += pop(stack)
            pop(stack) 
        elif is_operator(i):
            while not is_empty(stack) and precedence(i) <= precedence(peek(stack)):
                postfix += pop(stack)
            push(stack, i)
        else:
            postfix += i

        print("".join(stack) + " " + postfix)

    while not is_empty(stack):
        postfix += pop(stack)

    return postfix


def infix_to_prefix(infix):
    prefix = ""
    stack = []
    infix = infix[::-1]
    infix.append(")")
    stack.append("(")

    for i in infix:
        if i == ")":
            push(stack, i)
        elif i == "(":
            while peek(stack) != ")":
                prefix += pop(stack)
            pop(stack)
        elif is_operator(i):
            while not is_empty(stack) and precedence(i) < precedence(peek(stack)):
                prefix += pop(stack)
            push(stack, i)
        else:
            prefix += i
        print("stack" + ": " + "".join(stack) + " prefix string:  " + prefix)

    while not is_empty(stack):
        prefix += pop(stack)

    out = ""
    for i in prefix:
        if i != "(" and i != ")":
            out += i

    return out[::-1]


def postfix_to_value(postfix):
    stack = []
    for i in postfix:
        if is_operator(i):
            operand2 = pop(stack)
            operand1 = pop(stack)
            if i == "+":
                result = int(operand1) + int(operand2)
            elif i == "-":
                result = int(operand1) - int(operand2)
            elif i == "*":
                result = int(operand1) * int(operand2)
            elif i == "/":
                result = int(operand1) / int(operand2)
            elif i == "^":
                result = int(operand1) ** int(operand2)
            push(stack, result)
        else:
            push(stack, i)
    return pop(stack)

def prefix_to_value(prefix):
    stack = []
    for i in prefix[::-1]:
        if is_operator(i):
            operand1 = pop(stack)
            operand2 = pop(stack)
            if operand1.isdigit() and operand2.isdigit():  # Check if operands are digits
                operand1, operand2 = int(operand1), int(operand2)
                if i == "+":
                    result = operand1 + operand2
                elif i == "-":
                    result = operand1 - operand2
                elif i == "*":
                    result = operand1 * operand2
                elif i == "/":
                    result = operand1 / operand2
                elif i == "^":
                    result = operand1 ** operand2
                push(stack, str(result))
            else:
                return "Invalid operands"
        else:
            push(stack, i)
    return pop(stack)



infix_expression = input("Enter the infix expression: ")
infix_list = list(infix_expression.replace(" ", ""))
postfix_expression = infix_to_postfix(infix_list)
print("Postfix expression:", postfix_expression)


check = True
for i in postfix_expression:
    if i.isalpha():
        check = False
        break

if check:
    print("Value:", postfix_to_value(postfix_expression))
else:
    print("Value: N/A")

prefix_expression = infix_to_prefix(infix_list)
print("Prefix expression:", prefix_expression)

if check:
    print("Value:", prefix_to_value(prefix_expression))
else:
    print("Value: N/A")
