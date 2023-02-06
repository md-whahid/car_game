condition = ""
start = False
while condition != "quit":
    condition = input(">>> ").lower()
    if condition == "start":
        if start:
            print("car is already started!")
        else:
            start = True
            print("the car is started")
    elif condition == "stop":
        if not start:
            print("car is already stoped")
        else:
            start = False
            print("the car is stoped")
    elif condition == "quit":
        break
    elif condition == "help":
        print('''
        "start" =>> the car is started.....
        "stop" =>> the car is stoped......
        "quit" =>> the game will quit!.....''')
    else:
        print("sorry! i don'tunderstand")
