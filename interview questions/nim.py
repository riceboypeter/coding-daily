'''
Asked by Microsoft Shanghai for a summer student position. I failed this one (ToT)/~~~
- it doesn't matter which side goes first
- game starts with x sticks where x > 3
- players can take 1 or 2 sticks out of the pile
- last person to take something wins
- they wanted input checking
'''

# takes the userinput
def takeInput():
    userin = input("How many sticks to take (1 or 2): ")
    if userin:
        try:
            if int(userin) > 2 or int(userin) <= 0:
                print("aye not a valid number")
                return takeInput()
        except:
            print("that's not a number bub")
            return takeInput()
    elif not userin:
        print("don't just hit enter dawg")
        return takeInput()
    return int(userin)

def prepTurns():
    userin = input("First, second, or coinflip? (f/s/c): ")
    if userin:
        if userin in ["f","F","s","S","c","C"]:
            return
        else:
            print
            return takeInput()
    else:
        print("don't just hit enter dawg")
        return takeInput()

def main():
    # do setup for game here
    
    game = bool
    userin = takeInput()



    # do gameplay here


main()