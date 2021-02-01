#!/usr/bin/env python


def infix_to_postfix(infix, precedence):
    postfix = ""
    operators = []
    for token in infix:
        if token not in precedence:
            postfix += token
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators[-1] != "(":
                postfix += operators.pop()
            operators.pop()
        else:
            while operators and precedence[token] <= precedence[operators[-1]]:
                postfix += operators.pop()
            operators.append(token)
    while len(operators) > 0:
        postfix += operators.pop()
    return postfix


def eval_postfix(postfix, operators):
    stack = []
    for token in postfix:
        if token not in operators:
            stack.append(token)
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(eval(f"{left}{token}{right}"))
    return stack.pop()


def eval_infix(infix, precedence):
    return eval_postfix(
        infix_to_postfix(infix, precedence=precedence),
        operators=list(precedence.keys()),
    )


def answer(infix, part):
    if part == 1:
        precedence = {"*": 1, "+": 1, "(": 0, ")": 0}
    else:
        precedence = {"*": 1, "+": 2, "(": 0, ")": 0}
    return sum(eval_infix(expr, precedence) for expr in infix)


def read_infix(path):
    with open(path) as f:
        lines = f.read().strip().split("\n")
    return [line.replace(" ", "") for line in lines]


def main():
    infix = read_infix("input.txt")
    assert answer(infix, 1) == 4940631886147
    assert answer(infix, 2) == 283582817678281
    print("All tests passed.")


if __name__ == "__main__":
    main()
