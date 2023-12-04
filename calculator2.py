first=int(input('Enter First Number: '))
second=int(input('Enter Second Number: '))
operation=str(input("Enter Operation(+,-,*,/)"))

if operation == "+":
    total =first + second
elif operation == "*":
    total =first * second
elif operation == "-":
    total=first - second
elif operation == "/":
    total=first / second
else: 
    total=('Error,Please enter a valid statement.')
print(total)