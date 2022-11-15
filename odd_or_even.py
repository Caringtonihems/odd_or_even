while True:
    #welcome the user 
    print("Welcome to the odd or even game \n")
    # initialize variables, ask user would he or she like to play game
    rules = "you will enter a number i will check if the number is odd or even\nthen i will print out whether it is odd or even to you and ask if you'd like to play again"
    isplaying = input("Would you like to play? (type Yes or Y to play): ").upper()
    #if user did not type yes and user did not type y end game
    if isplaying != "YES" and isplaying != "Y": #this if statement checks to see if the user has entered either yes or y 
        print("see you later")
        quit()
    #print out the rules to the user
    print ("good welcome to the game i will explain the rules \n%s" % (rules))
    #prompt user to enter their number
    number = int(input("whats your number?: "))
    
    #if number dived by 2 gives no remainder then its even else its odd
    if number % 2 == 0:
        print("the number you entered is an even number")
    else:
        print("the number that you entered is an odd number")
    
    #ask user if theyd like to play again
    again = input("would you like to play again? (type Yes or Y to play again): ").upper()

    # if the user says yes or y then dont quit else quit
    if again == "YES" or again == "Y": #this if statement checks to see if the user has entered either yes or y 
        print("Restarting")
    else:
        print("cyaaaa :) ")
        quit()     




    
