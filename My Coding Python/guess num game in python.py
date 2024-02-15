name=input("Enter your name : ")
print("Hi", name ,"this is a guess the integer number game")
while True:
    a=int(input("Enter a guess number : "))
    if (a>17):
        print(name,"your guess is high please try again...")
    elif (a<17):
        print(name,"your guess is low please try again...")
    else:
        print("cool your guess is correct",name)
        if (a==17):
            break
print("Thanks playing this game",name)
    
