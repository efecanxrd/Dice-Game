import random

while True:
    game = input("Press y to play rolling dice. >> ")
    if game.lower() == "y":
        y = 0
        userwins = 0
        compwins = 0
        draws = 0
        while(y < 5):
            User = random.randint(1,6)
            Comp = random.randint(1,6)
            if User > Comp:
                print (f"User wins! {User} vs {Comp}")
                userwins += 1
            elif User < Comp:
                    print(f"Computer wins! {Comp} vs {User}")
                    compwins += 1
            if User == Comp:
                print(f"Draw, no winner! {Comp} vs {User}")
                draws += 1
            y += 1
        print(' ')
        print("Reporting the results:")
        print("Total number of dice rolls: 5")
        print(f"The user won {userwins} times.")
        print(f"The computer won {compwins} times.")
        print(f"The draws were {draws} times.")

    else:
        print ("The game has ended.")
        exit(0)