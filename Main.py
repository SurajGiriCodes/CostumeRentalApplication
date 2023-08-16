import Rent
import Return
import Display

Display.welcome()
continueLoop = True
while continueLoop == True:
    Display.options()
    continueCorrectOption = False
    while continueCorrectOption == False:
        try:
            option = int(input("Enter a option: "))
            continueCorrectOption = True
        except:
            Display.invalid_options()
            Display.options()

    if option == 1:
        Rent.rent_costume()   
    elif option == 2:
        Return.return_costume()
    elif option == 3:
        Display.Exit()
        continueLoop = False 
    else:
        Display.Invalid()
