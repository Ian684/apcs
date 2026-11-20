def solve(tokens):
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            right, left = stack.pop(), stack.pop()
            stack.append({'+': left + right, '-': left - right, '*': left * right, '/': int(left / right)}[token])
    return stack[-1]

if __name__ == "__main__":
    print("Exercise: 10_postfix_calculator")
