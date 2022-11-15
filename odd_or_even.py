while True:
    print("Welcome to the odd or even game \n")

    rules = "you will enter a number i will check if the number is odd or even\nthen i will print out whether it is odd or even to you and ask if you'd like to play again"
    isplaying = input("Would you like to play? (type Yes or Y to play): ")
    isplaying = isplaying.upper()

    if isplaying != "YES" and isplaying != "Y": #this if statement checks to see if the user has entered either yes or y 
        print("see you later")
        quit()

    print ("good welcome to the game i will explain the rules \n%s" % (rules))

    number = int(input("whats your number?: "))

    if number % 2 == 0:
        print("the number you entered is an even number")
    else:
        print("the number that you entered is an odd number")

    again = input("would you like to play again? (type Yes or Y to play again): ")
    again = again.upper()

    if again == "YES" or again == "Y": #this if statement checks to see if the user has entered either yes or y 
        print("Restarting")
    else:
        print("cyaaaa :) ")
        quit()     




    