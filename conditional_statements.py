age = 21
if age >= 18:
    print("You can vote")
else:
    print("You can't vote")

username = input("Enter username:")
password = input("Enter password:")
if username == "admin" and password == "pass":
    print("Login Successful")
elif username != "admin":
    print("Wrong username")
else:
    print("Wrong password")

# Match case
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
