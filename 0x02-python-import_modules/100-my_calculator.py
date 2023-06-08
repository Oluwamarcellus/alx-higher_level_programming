#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    import sys
    if len(sys.argv) == 4:
        op = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if op != '+' and op != '-' and op != '*' and op != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if op == '+':
                print("{} {} {} = {}".format(a, op, b, add(a, b)))
            elif op == '-':
                print("{} {} {} = {}".format(a, op, b, sub(a, b)))
            elif op == '*':
                print("{} {} {} = {}".format(a, op, b, mul(a, b)))
            else:
                print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
