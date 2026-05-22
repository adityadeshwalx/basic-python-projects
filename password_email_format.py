import re
import json

email_pattern = r'^[a-zA-Z0-9_]+@\w+\.\w{2,}$'

email = input("Enter Email: ")

if re.match(email_pattern, email):
    print("Email matched!")
else:
    print("Wrong Email!")
    exit()
    
password_pattern = r'^(?=.*[A-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,20}$'

password = input("Enter Password: ")

if re.match(password_pattern, password):
    print("Password matched!")
else:
    print("Please try again!")
    exit()

newUser = {
    "email": email,
    "password": password
}

try:
    with open("users.json", "r") as users_file:
        users = json.load(users_file)
except:
    users = []
users.append(newUser)
with open("users.json", "w") as users_file:
    json.dump(users, users_file, indent=4)

print("User saved successfully!")