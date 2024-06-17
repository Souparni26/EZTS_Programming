s = input()
op = ["+", "-", "*", "/", "//", "%"]
for i in s:
    if i in op:
        x = i
        s = s.replace(i, " ")
l = list(map(float, s.split(" ")))

# Perform arithmetic operation
result = None
if x == '+':
    result = l[0] + l[1]
elif x == '-':
    result = l[0] - l[1]
elif x == '*':
    result = l[0] * l[1]
elif x == '/':
    result = l[0] / l[1]
elif x == '//':
    result = l[0] // l[1]
elif x == '%':
    result = l[0] % l[1]

# Convert result to string
if result is not None:
    result = str(result)

# Print result and operation
print("Operation:", end=" ")
match x:
    case '+':
        print("addition")
    case '-':
        print("subtraction")
    case "*":
        print("multiplication")
    case "/":
        print("division")
    case "//":
        print("float division")
    case "%":
        print("modus")
print("Result:",result)
