# 1. Input name & age and print message
name = input("enter name:")
age = int(input("enter age:"))
print("Hello", name, "You are", age, "Years old")

# 2. Perform arithmetic operations
a = int(input("Enter First number:"))
b = int(input("Enter Second number:"))
print("Sum is:", (a + b))
print("Difference is:", (a - b))
print("Product is:", (a * b))
print("Quotient is:", (a / b))

# 3. Average of two integers and one float
n1 = int(input("Enter an integer:"))
n2 = int(input("Enter an integer:"))
n3 = float(input("Enter a float:"))
print("avg =", (n1 + n2 + n3) / 3)

# 4. Typecasting string into int, float, and string
str1 = "45"
i = int(str1)  # converting to integer
print(i, type(i))
f = float(str1)  # converting to float
print(f, type(f))
s = str(str1)  # converting to string
print(s, type(s))

# 6. Swapping two numbers using a temporary variable
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
temp = num1
num1 = num2
num2 = temp
print(num1, num2)

# 7. Convert Celsius to Fahrenheit
temp = input("Enter temperature in celcius:")
temp1 = float(temp)
print("Ftemp:", (temp1 * (9 / 5)) + 32)

# 8. Calculate the area of a circle
rad = int(input("Enter a radius:"))
PI = 3.14
print("Area:", (PI * rad**2))

# 9. Calculate Simple Interest
P = int(input("Enter a principal:"))
R = int(input("Enter a rate:"))
T = int(input("Enter a time:"))
print("SI is:", float((P * R * T) / 100))

# 10. Extract integer and decimal part from float
num = 45.78
integer_part = int(num)  # integer part
decimal_part = str(num).split(".")[1]  # fractional digits
print("Integer part:", integer_part)
print("Decimal part:", decimal_part)

