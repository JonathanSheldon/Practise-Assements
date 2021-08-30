#Allows the programs to create a date and timestamp
import datetime
today=datetime.datetime.now()

def force_name(message,lower,upper):
    while True: #Infinite loop that will keep repeating until the if statement is met
        name=str(input(message)).title() #Personalised input message which is passed as a parameter
        if len(name)>=lower and len(name)<=upper and name.isalpha(): #Ensures name is 2-20 characters and A-Z
            break
        else:
            print("ERROR.{}, please enter text only".format(message))
    return name #This returns a valid name that is 2-20 characters and A-Z

def get_phone_number(message): #Runs a message through this program
    while True: #While true loop to filter bad data
        try:
            phone_number = str(input(message)) #asks for phone number or 0 to quit.
            if len(phone_number) >= 9 and len(phone_number) <=12 and phone_number.isnumeric():
                break #Breaks the function if specifications are met
            else: #If specs aren't met will run this
                print("Cellphone numbers only contain numbers and are between 9 and 12 digits") #Tells the user the parameters for entering a phone number
        except:
            print("Please enter a valid phone number") #Tells user to enter correct phone number
    return phone_number #Will return value to variable that called the function

#Create a subroutine for breadtype
def breads ():
    global breadtype, breadlist
    breadlist = ["White", "Brown", "Italian", "Granary"]
    breadcount = 0
    print("We have the following breads!")
    while breadcount <4:
        print (breadcount,"     ",breadlist[breadcount])
        breadcount = breadcount + 1
    breadtype = int(input("What number bread do you want?"))

def meats ():
    global meattype, meatlist
    meatlist = ["Chicken", "Turkey", "Tuna", "Bacon"]
    meatcount = 0
    print("We have the following meats!")
    while meatcount <4:
        print (meatcount,"     ",meatlist[meatcount])
        meatcount = meatcount + 1
    meattype = int(input("What number meat do you want?"))

def cheeses ():
    global cheesetype, cheeselist
    cheeselist = ["Swiss", "Feta", "Brie", "Tasty"]
    cheesecount = 0
    print("We have the following cheeses!")
    while cheesecount <4:
        print (cheesecount,"     ",cheeselist[cheesecount])
        cheesecount = cheesecount + 1
    cheesetype = int(input("What number cheese do you want?"))

#Create a subroutine for salads
def salads ():
    global saladtype, saladlist, saladswanted
    saladlist = ["Lettuce", "Tomato", "Carrot", "Cucumber", "Onions"]
    saladcount = 0
    print("We have the following salads, you can have as many as you want")
    while saladcount < 5:
        print(saladcount, "     ",saladlist[saladcount])
        saladcount = saladcount + 1
    print("Press ENTER when you have finished choosing your salads")
    saladswanted = ""
    saladtype = "   "
    while saladtype != "":
        saladtype = input("What number salad do you want?")
        if saladtype != "":
            saladtype = int(saladtype)
            saladswanted = saladswanted + " " + saladlist[saladtype]

def output_order():
    breadorder=[]
    #This adds the persons entire order details to the list
    breadorder.append(first_name)
    breadorder.append(cellphone)
    breadorder.append(breadlist[breadtype])
    breadorder.append(meatlist[meattype])
    breadorder.append(cheeselist[cheesetype])
    breadorder.append(saladswanted)
    breadorder.append(today)
    outputFile = open("orders.txt", "a") #Opens text file
    print("********** Order for {} - {} **********".format(first_name, cellphone))
    outputFile.write("********** Order for {} - {} **********".format(first_name, cellphone))
    for order in breadorder:
        print(order)
        outputFile.write("{}\n".format(order))
    outputFile.write("********** End of Order: {}. **********".format(today))
    print("********** End of Order: {}. **********".format(today))
    outputFile.close()

#Main Program that makes calls to the other functions
first_name = force_name("Please enter in your first name",2,10)
cellphone = get_phone_number("Please enter in your cellphone")
breads()
meats()
cheeses()
salads()
output_order()