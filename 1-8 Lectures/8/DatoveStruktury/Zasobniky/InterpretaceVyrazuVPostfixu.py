def evaluate_postfix(expression):
    stack = []

    def apply_operator(operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2

    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            # If the token is a number, push it onto the stack
            stack.append(float(token))
        else:
            # If the token is an operator, pop operands from the stack, apply the operator, and push the result back
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(token, operand1, operand2)
            stack.append(result)

    # The final result should be on the top of the stack
    return stack[0]

# Test
postfix_expression = "7 8 * 2 6 * + 5 +"
result = evaluate_postfix(postfix_expression)
print("Result:", result)
