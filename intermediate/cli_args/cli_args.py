# Command Line Argument Processing using argparse in Python

import argparse

def main():
    # 1. Create the parser
    parser = argparse.ArgumentParser(description="A simple calculator program using command line args.")

    # 2. Add arguments
    # Positional arguments (required)
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    
    # Optional arguments (with default values or actions)
    parser.add_argument("--operation", default="add", choices=["add", "sub", "mul", "div"],
                        help="Operation to perform (default: add)")

    # 3. Parse arguments
    args = parser.parse_args()

    # 4. Perform calculation based on args
    n1 = args.num1
    n2 = args.num2
    op = args.operation

    if op == "add":
        res = n1 + n2
    elif op == "sub":
        res = n1 - n2
    elif op == "mul":
        res = n1 * n2
    elif op == "div":
        if n2 == 0:
            res = "Error: Division by zero!"
        else:
            res = n1 / n2

    print(f"Result of {op} on {n1} and {n2} is: {res}")

if __name__ == "__main__":
    main()
