# Check voting eligibility
age = 21
if age >= 18:
    print("You can vote")
else:
    print("You can't vote")

# Username and password login system
username = input("Enter username:")
password = input("Enter password:")
if username == "admin" and password == "pass":
    print("Login Successful")
elif username != "admin":
    print("Wrong username")
else:
    print("Wrong password")

# Match-case example (Python 3.10+)
color = input("Enter the color:")
match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _:
        print("Wrong colour")

# Print multiplication table of a given number
i = 1
n = int(input("Enter your number:"))
while i <= 10:
    print(n, "*", i, "=", n * i)
    i = i + 1

# Loop through a string and print each character
string = "muskan"
for var in string:
    print(var)

# Count occurrences of letter 'i' in the word
word = "artificial intelligence"
count = 0
for var in word:
    if var == "i":
        count += 1
print(count)

# Count total vowels in a word
nword = "artificial"
cnt = 0
for ch in nword:
    if ch in "AEIOUaeiou":
        cnt = cnt + 1
print(cnt)

# Sum of first N natural numbers
n = int(input("Enter a number:"))
sum = 0
for i in range(n + 1):
    sum += i
print("Sum of", n, "natural numbers is:", sum)


# Function to print a message
def printHello():
    print("Hello")


printHello()


# Function to calculate average of three numbers
def average(a, b, c):
    return (a + b + c) / 3


print(average(2, 3, 5))

# Lambda function to add two numbers
sum = lambda a, b: a + b
print(sum)
