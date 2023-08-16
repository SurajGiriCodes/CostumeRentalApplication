#importing datetime, random, display, rentfunc
import datetime
import random
import Display
import rentfunc

#defining the function
def rent_costume():
    Display.Rent()
    rentfunc.function()#calling the function()
    rentfunc.dictionary_rent()#calling the dictionary_rent()
    dictionaryCostume = rentfunc.dictionary_rent()
    rentCostumeID = rentfunc.valid_costume_ID()
    rented_costumes = []
    items_brand = []
    if int(dictionaryCostume[rentCostumeID][3]) > 0:
        Display.costume_available()
        qty = rentfunc.quantity(int(dictionaryCostume[rentCostumeID][3]))
        dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3])- qty
        print(dictionaryCostume)
        
        customer_name = input("\nEnter the name of customer: ")
        
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        price = rentfunc.Total_price(dictionaryCostume,qty,rentCostumeID)
        
        rented_costumes.append(dictionaryCostume[rentCostumeID][0])
        rentfunc.stock_costume(dictionaryCostume)
        
        items_brand.append(dictionaryCostume[rentCostumeID][1])
        rentfunc.stock_costume(dictionaryCostume)
        
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Does the customer want to rent another costume as well??")
        rentMORE = input("Please enter 'Y' if the customer wants to rent another costume else provide any other value: ").upper()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")        
        loop = True
        while loop == True: 
            if rentMORE == "Y":
                Display.Rent()
                rentfunc.function()
                dictionaryCostume = rentfunc.dictionary_rent()
                rentCostumeID = rentfunc.valid_costume_ID()
                
                if int(dictionaryCostume[rentCostumeID][3]) > 0:
                    Display.costume_available()
                    
                    qty = rentfunc.quantity(int(dictionaryCostume[rentCostumeID][3]))
                    dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3]) - qty
                    print(dictionaryCostume)
                    
                    rented_costumes.append(dictionaryCostume[rentCostumeID][0])#appending
                    rentfunc.stock_costume(dictionaryCostume)
                    
                    items_brand.append(dictionaryCostume[rentCostumeID][1])#appending
                    rentfunc.stock_costume(dictionaryCostume)
                    
                    price = rentfunc.Total_price(dictionaryCostume,qty,rentCostumeID) + price
                    
                    print()
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("Does the customer want to rent another costume as well??")
                    rentMORE = input("Please enter 'Y' if the customer wants to rent another costume else provide any other value: ").upper()
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  

            else:
                print()
                print("====================================================")
                print("                    Bill Details                    ")
                print("====================================================")
                print("****************************************************")
                print("Name of Customer: ", customer_name)
                print()
                print("Date and time of rent: ", date_time)
                print()
                print("Total Price: $", price)
                print()
                print("Items Rented are: ",", ".join(rented_costumes))
                print()
                print("Brand of the Items are: ",", ".join(items_brand))
                print("****************************************************")
                print()
                print("+++++++++++++++++++++++++++++++++++++++++++++++++")
                print("|     Rent Details Bill has been generated.     |")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++")
                print()

                #generating bill
                num=str(random.randint(999999999,9999999999))
                bill = open("Rent_"+customer_name+"_"+num+".txt","w")
                bill.write("===============================================\n")
                bill.write("                   Invoice                    \n")
                bill.write("===============================================\n")
                bill.write(" Name of Customer: " + str(customer_name))
                bill.write("\n Date and time of rent: " +str(date_time))
                bill.write("\n Total Price: $" + str(price))
                bill.write("\n Items rented are: " + ", ".join(rented_costumes))
                bill.write("\n Brand of the Items are: " +", ".join(items_brand))
                bill.write("\n===============================================")
                bill.close()
                loop = False
    else:
        Display.costume_unavailable() #calling costume_unavailable() 
