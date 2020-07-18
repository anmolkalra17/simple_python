n1 = float(input())
n2 = float(input())
op = input()

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "/":
    if n2 == 0.0:
        print("Division by 0!")
    else:    
        print(n1 / n2)
elif op == "*":
    print(n1 * n2)

elif op == "mod":
    if n2 == 0.0:
        print("Division by 0!")
    else:    
        print(n1 % n2)
elif op == "pow":
    if n2 == 0.0:
        print("Division by 0!")
    else:    
        print(n1 ** n2)
elif op == "div":
    if n2 == 0.0:
        print("Division by 0!")
    else:    
        print(n1 // n2)
