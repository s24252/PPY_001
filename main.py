# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

# task 1
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
print("Name: ", name)
print("Surame: ", surname)
print("Age: ", age)
# task 2
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print("Temerature in Celcius: ", celsius)
#task 3
score = float(input("Enter your score: "))

if score >= 90:
    grade = "5"
elif score >= 80:
    grade = "5"
elif score >= 70:
    grade = "4"
elif score >= 60:
    grade = "4"
elif score >= 50:
    grade = "project"
elif score >= 30:
    grade = "test"
elif score >= 20:
    grade = "work in class"
else:
    grade = "2"

print("Your grade is:", grade)
# task 4
number = int(input("Enter a number: "))
number2 = int(input("Enter second number"))

if number % number2 == 0:
  result = "diveded"
else:
  result = "not devided"
print("The number is", result)
#task 7
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
      result = "Invalid operation"
    else:
      result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)