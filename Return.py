import datetime
import random
import Display
import returnfunc

def return_costume():
    Display.Return()
    returnfunc.log()
    returnfunc.dictionary_return()
    dictionaryCostume = returnfunc.dictionary_return()
    returnCostumeID = returnfunc.valid_costume_ID()
    rented_costumes = []
    items_brand = []
    
    
    (int(dictionaryCostume[returnCostumeID][3]) > 0)
    qty = returnfunc.quantity(int(dictionaryCostume[returnCostumeID][3]))
    dictionaryCostume[returnCostumeID][3] = int(dictionaryCostume[returnCostumeID][3]) + qty
    print()
    print(dictionaryCostume)

    
    days = int(input("\nHow many days have you rented the costume: "))
    total_fine = 0
    if days<=5:
        fine_days = 0
    elif days>5:
        fine_days=days-5
        total_fine += (fine_days * 10)
        print("The total fine is: $", total_fine)
    
    customer_name = input("\nEnter the name of customer: ")
    
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
    rented_costumes.append(dictionaryCostume[returnCostumeID][0])
    returnfunc.stock_costume(dictionaryCostume)
    
    items_brand.append(dictionaryCostume[returnCostumeID][1])
    returnfunc.stock_costume(dictionaryCostume)
    
            
    print()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Have the customer rented another costume as well??")
    returnMORE = input("Please enter 'Y' if the costume has to be returned else provide any other value: ").upper()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")        
    loop = True
    while loop == True:
        if returnMORE == "Y":
            Display.Return()
            returnfunc.log()
            dictionaryCostume = returnfunc.dictionary_return()
            returnCostumeID = returnfunc.valid_costume_ID()
            
            int(dictionaryCostume[returnCostumeID][3]) > 0
            qty = returnfunc.quantity(int(dictionaryCostume[returnCostumeID][3]))
            dictionaryCostume[returnCostumeID][3] = int(dictionaryCostume[returnCostumeID][3]) + qty
            print()
            print(dictionaryCostume)
            
            days = int(input("\nHow many days have you rented the costume: "))
            if days<=5:
                fine_days = 0
            elif days>5:
                fine_days=days-5
                total_fine += (fine_days * 10)
                print("The total fine is: $", total_fine)
            
            rented_costumes.append(dictionaryCostume[returnCostumeID][0])
            returnfunc.stock_costume(dictionaryCostume)
            
            items_brand.append(dictionaryCostume[returnCostumeID][1])
            returnfunc.stock_costume(dictionaryCostume)
                                
            print()
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Have the customer rented another costume as well??")
            returnMORE = input("Please enter 'Y' if the costume has to be returned else provide any other value: ").upper()
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")   
        else:
            print()
            print("====================================================")
            print("                    Bill Details                    ")
            print("====================================================")
            print("****************************************************")
            print("Name of Customer: ", customer_name)
            print()
            print("Date and time of Return: ", date_time)
            print()
            print("Total Fine: $", total_fine)
            print()
            print("Items Returned are: ", ", ".join(rented_costumes))
            print()
            print("Brand of the Items are: ",", ".join(items_brand))
            print("****************************************************")
            print()
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("|     Return Details Bill has been generated.     |")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
            print()
            
            num=str(random.randint(999999999,9999999999))
            bill = open("Return_"+customer_name+"_"+num+".txt","w")
            bill.write("==============================================\n")
            bill.write("                   Invoice                    \n")
            bill.write("==============================================\n")
            bill.write("Name of Customer: " + str(customer_name))
            bill.write("\nDate and time of Return: " +str(date_time))
            bill.write("\nTotal Fine: $" +str(total_fine))
            bill.write("\nItems returned are: " + ", ".join(rented_costumes))
            bill.write("\nBrand of the Items are: " +", ".join(items_brand))
            bill.write("\n==============================================")
            bill.close()
            loop = False
