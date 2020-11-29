from art import logo


def add(n1, n2):
    return n1+n2


def subtract(n1,n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
print(logo)
num1 = int(input("What is the first number: "))
num2= int(input("what is the second number: "))

for key in operations:
    print(key)

key = input("Pick an operation from the line above: ")
result = operations[key]
print(result(num1, num2))
