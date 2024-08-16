exp = input()

def add(a,b):
    return int(a) + int(b)

def sub(a, b):
    return int(a) - int(b)

def mul(a, b):
    return int(a) * int(b)

def div(a, b):
    if b == '0':
        print("Invalid Operation")
    else :
        return int(a) / int(b)
    
x = exp.split(" ")

if x[1] == '+':
    print(add(x[0], x[2]))
elif x[1] == '-':
    print(sub(x[0], x[2]))
elif x[1] == '*':
    print(mul(x[0], x[2]))
elif x[1] == '/':
    print(div(x[0], x[2]))

