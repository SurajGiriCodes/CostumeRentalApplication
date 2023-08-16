import Display

def function():
    file = open("costumes.txt","r")
    print("----------------------------------------------------------")
    print("  ID\tCustomer Name\tCostume Brand\tPrice\tQuantity")
    print("----------------------------------------------------------")
    counterID = 0
    for line in file:
        counterID = counterID + 1
        print(" ",counterID, "\t" + line.replace(",","\t"))
    file.close()
    print("----------------------------------------------------------")

def dictionary_rent():
    file = open("costumes.txt", "r")
    counterID = 0
    dictionaryCostume = {}
    for line in file: 
        counterID = counterID + 1
        line = line.replace("\n","")
        line = line.split(',')
        dictionaryCostume[counterID] =  line
    return dictionaryCostume

def valid_costume_ID():
    try:
        costumeID = int(input("Enter the ID of costume you want to rent: "))
        while costumeID <= 0 or costumeID > len(dictionary_rent()):
            Display.valid()
            function()
            costumeID = int(input("\nEnter the ID of costume you want to rent: "))
        return costumeID
    except:
        Display.Invalid_input()
        valid_costume_ID()
        
def quantity(stock):
    error = False
    while error == False:
        try:
            qty = int(input("Enter the quantity: "))
            while qty <=0 or qty > stock:
                if qty <= 0:
                    Display.valid_quantity()
                else:
                    Display.more_quantity()
                qty = int(input("Enter the quantity: "))
            return qty
            error = True
        except:
            Display.Invalid()
        
def stock_costume(dictionary):
    file = open("costumes.txt","w")
    for i in dictionary.values():
        line = str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3])) 
        file.write(line)
        file.write("\n")
    file.close()

def Total_price(dictionary, quantityDetails, rentCostumeID):
    price = float(dictionary[rentCostumeID][2].replace("$",""))
    print("\nThe price of costume:", price)
    pricePerItem = price * quantityDetails
    return pricePerItem

