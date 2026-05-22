import json

print("1. Signup")
print("2. Login")

a=int(input("what do you want to do :"))

if a==1 : 

    email = input("Email: ")
    password = input("password: ")

    newUser = {"email": email, "password": password, "task": []}

    with open("./users.json", "r") as users_file:
        users_json = users_file.read()
        users = json.loads(users_json)

    users.append(newUser)
    users_json = json.dumps(users, indent=4)

    with open("./users.json", "w") as users_file:
        users_file.write(users_json)

        print("Signup successful ✅")

elif a==2:
    
    with open("./users.json", "r") as users_file:
        users_json = users_file.read()
        users = json.loads(users_json)
        
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    logged_in = None

    for user in users:
         if user["email"] == email and user["password"] == password:
             logged_in = user
             break

    if logged_in:
         print("Login Successful! Welcome✅", email)
         while True:
            print("1. Add task")
            print("2. Logout")

            b = int(input("Choose an option: "))

            
            if b == 1:
                task = input("Enter new task: ")
                logged_in["task"].append(task)

                with open("./users.json", "w") as users_file:
                    json.dump(users, users_file, indent=4)
                
                print("Task added ✅")

            elif b == 2:
                print("Logged out 👋")
                break   

    else:
         print("Invalid email or password❌")



