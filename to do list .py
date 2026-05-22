while True:
    task=input("what do you want to do:")
    if task == "create":
        a = input("File name: ")
        b = input("Write something: ")
        with open(a, "w") as file:
            file.write(b)
        print("Created")
    elif task == "read":
        a = input("file name:")
        with open (a , "r") as file:
            print(file.read())
    elif task=="append":
        a=input("file name:")
        b=input("add text:")
        with open(a,"a") as file:
            file.write("\n"+ b) 
            print("appeded")
    elif task=="delete":
        a=input("file name:")
        import os
        os.remove(a)
        print("delete")
    elif task=="exit":
        break
    