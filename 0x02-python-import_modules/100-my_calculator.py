#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mult, div

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mult(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
