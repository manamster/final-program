#Calvin Comstock-Fisher
#11/14/20
#Cash Register Program

#Step 1: Import Tkinter
import tkinter as tk

#Step 2: Define the main window with parameters
window = tk.Tk()
window.minsize(640,480)
window.title("Cash Register")
#Step 2.1: Woo I made a custom sprite for the icon in the title bar :)
icon = tk.PhotoImage(file="icon.png")
window.iconphoto(False, icon)

#Step 3: Create global variables for use in calculations in functions
customerServed = 0
subTotal = 0.0
tax = 0
totalAT = 0
totalDaySales = 0
totalDayTax = 0
dayTotal = 0
#Step 3.1: Nice dictionaries. These make my life easier and I am happy we got to them this semester :)
prices = {"hamburger":1.29,"fries":0.99,"onionrings":1.09,"smallsoftdrink":0.79,"largesoftdrink":1.19,"cheese":0.75,"lettuce":0.3,"ketchup":0.2,"onion":0.4,"tomato":0.5,"bacon":0.6}
numSold = {"hamburger":0,"fries":0,"onionrings":0,"smallsoftdrink":0,"largesoftdrink":0,"cheese":0,"lettuce":0,"ketchup":0,"onion":0,"tomato":0,"bacon":0}

#Step 4: Create the add price function which calculates the Sub Total and increases the counter for the number of items that the restaurant sells that day
def addPrice(item, flag):
    #Step 4.1: Gets access to global variable for editing
    global subTotal
    #Step 4.2: Have a flag that makes the function do 2 tasks 1.Add to sub total 2.Return the subtotal from anywhere to make life easier in other functions
    if flag == 1:
        return subTotal
    else:
        pass
    #Step 4.3: Allow access to the global prices dictionary
    global prices
    try:
        #Step 4.3.1: Add the price of the specified item that was passed through by the button to the sub total
        subTotal += prices[item]
        numSold[item] += 1
    except:
        pass

#Step 5: Create the main page that shows up when you first launch the program
def firstPage():
    #Step 5.1: Creates the overarching frame that holds the other frames for the buttons
    overarchFrame.pack()
    introLabel.pack()
    #Step 5.2L: Creates the first button frame that holds the food
    buttonFrame.pack(pady=5)
    #Step 5.3: Packs all the buttons in a line
    hamButton.pack(side="left")
    friesButton.pack(side="left")
    onionButton.pack(side="left")
    smallSDButton.pack(side="left")
    largeSDButton.pack(side="left")
    #Step 5.4: Creates the 2nd button frame that hold the price checking buttons
    buttonFrame2.pack()
    #Step 5.5: Pack em
    endOrderButton.pack(side="top")
    saleReportButton.pack(side="top")

#Step 6: Create a function that brings the user back to the first page from any other page
def backFirstPage():
    #Step 6.1: Tries to destroy every page and uses try statements to prevent erroring out
    try:
        overarchFrame2.pack_forget()
    except:
        pass
    try:
        overarchFrame3.pack_forget()
    except:
        pass
    try:
        overarchFrame4.pack_forget()
    except:
        pass
    try:
        overarchFrame5.pack_forget()
    except:
        pass
    #Step 6.2: Creates the first page
    firstPage()

#Step 7: Forgets the first page so that the user can go to other pages.
def destoryFirstPage():
    overarchFrame.pack_forget()

#Step 8: Creates the function for the end order button to use
def endOrder(tempVal):
    #Step 8.1: Destroys first page
    destoryFirstPage()
    #Step 8.2: Packs first frame
    overarchFrame3.pack()
    #Step 8.3: Allows the use of all the needed global variables
    global tax
    global totalAT
    global totalDaySales
    global totalDayTax
    global customerServed
    global dayTotal
    #Step 8.4: Does the math that calcualates most of those global variables
    customerServed +=1
    tax = tempVal * 0.05
    totalDayTax += tax
    totalAT = tempVal + tax
    dayTotal += totalAT
    totalDaySales += tempVal
    #Step 8.5: Prints all the totals for that order
    subTotalLabel = tk.Label(overarchFrame3, text="{:<10}{:>10}{:<10,.2f}".format("Subtotal:", "$", subTotal)).pack()
    taxLabel = tk.Label(overarchFrame3, text="{:<10}{:>10}{:<10,.2f}".format("Tax:", "$", tax)).pack()
    totalLabel = tk.Label(overarchFrame3, text="{:<10}{:>10}{:<10,.2f}".format("Total:", "$", totalAT)).pack()
    #Step 8.6: Allows the user to go to the next customer function
    nextCustomerButton.pack()

#Step 9: Creates the hamburger toppings page.
def hamburgerToppingsPage():
    #Step 9.1: Destroys first page
    destoryFirstPage()
    #Step 9.2: Packs the beginning frame and label
    overarchFrame2.pack()
    toppingsLabel.pack()
    #Step 9.3: Makes sure that the price of the hamburger is added even if there are no toppings added
    addPrice("hamburger",0)
    #Step 9.4: Adds all the buttons to the page for choosing toppings and exiting
    buttonFrameHamburger.pack()
    cheeseTopping.pack(side="left")
    lettuceTopping.pack(side="left")
    ketchupTopping.pack(side="left")
    onionTopping.pack(side="left")
    tomatoTopping.pack(side="left")
    baconTopping.pack(side="left")
    buttonFrameHamburger2.pack()
    exitButton.pack()

#Step 10: Creates the next customer page after they have finished ordering.
def nextCustomerPage():
    #Step 10.1: Goes back to first page then destroys it and load in the new page to prevent bugs
    backFirstPage()
    destoryFirstPage()
    #Step 10.2: Pack all items on page
    overarchFrame4.pack()
    instructionLabel.pack()
    amountCollected.pack()
    #Step 10.3: Make the function for checking money that runs when the exit button is pressed.
    def checkMoney():
        #Step 10.3.1: Allows the use of the global variable totalAT in this function
        global totalAT
        #Step 10.3.2: Checks the amount collected from customer and makes sure that the correct change is given/correct amount collected and it wont let the user leave this page until it is fixed.
        if float(amountCollected.get()) < round(totalAT,2):
            warningLabel = tk.Label(overarchFrame4, text="This is not enough please get the correct amount from the customer.").pack()
        elif float(amountCollected.get()) > round(totalAT,2):
            change = float(amountCollected.get()) - totalAT
            changeLabel = tk.Label(overarchFrame4, text="This is too much the amount of change owed is $" + str(round(change,2)) + ".").pack()
        elif float(amountCollected.get()) == round(totalAT,2):
            backFirstPage()
    #Step 10.4: Runs the previous function to prevent loss of money
    exitButton2 = tk.Button(overarchFrame4, text="Back to first page", command=checkMoney).pack()

#Step 11: Creates the sales report page
def salesReportPage():
    #Step 11.1: Destroys first page
    destoryFirstPage()
    #Step 11.2: Packs everything in because of a bug where it would grab the values before being called I couldnt do it outside the function
    overarchFrame5.pack()
    headerLabel = tk.Label(overarchFrame5, text="{:<30}{:<30}{:<30}".format("Item:","Qunatity","Sales:")).pack()
    hamLabel = tk.Label(overarchFrame5, text="{:<30}{:<30}{:<30}".format("Hamburger:",numSold["hamburger"],numSold["hamburger"]*prices["hamburger"])).pack()
    friesLabel = tk.Label(overarchFrame5, text="{:<39}{:<30}{:<30}".format("Fries:",numSold["fries"],numSold["fries"]*prices["fries"])).pack()
    onionRingsLabel = tk.Label(overarchFrame5, text="{:<31}{:<30}{:<30}".format("Onion Rings:",numSold["onionrings"],numSold["onionrings"]*prices["onionrings"])).pack()
    smallSoftDrinkLabel = tk.Label(overarchFrame5, text="{:<30}{:<30}{:<30}".format("Small Soft Drink:",numSold["smallsoftdrink"],numSold["smallsoftdrink"]*prices["smallsoftdrink"])).pack()
    largeSoftDrinkLabel = tk.Label(overarchFrame5, text="{:<30}{:<30}{:<30}".format("Large Soft Drink:",numSold["largesoftdrink"],numSold["largesoftdrink"]*prices["largesoftdrink"])).pack()
    toppingsTotalLabel = tk.Label(overarchFrame5, text="These are the toppings sold.").pack()
    cheeseLabel = tk.Label(overarchFrame5, text="{:<39}{:<30}{:<30}".format("Cheese:",numSold["cheese"],numSold["cheese"]*prices["cheese"])).pack()
    lettuceLabel = tk.Label(overarchFrame5, text="{:<39}{:<30}{:<30}".format("Lettuce:",numSold["lettuce"],numSold["lettuce"]*prices["lettuce"])).pack()
    ketchupLabel = tk.Label(overarchFrame5, text="{:<39}{:<30}{:<30}".format("Ketchup:",numSold["ketchup"],numSold["ketchup"]*prices["ketchup"])).pack()
    onionLabel = tk.Label(overarchFrame5, text="{:<39}{:<30}{:<30}".format("Onion:",numSold["onion"],numSold["onion"]*prices["onion"])).pack()
    tomatoLabel = tk.Label(overarchFrame5, text="{:<39}{:<30}{:<30}".format("Tomato:",numSold["tomato"],numSold["tomato"]*prices["tomato"])).pack()
    baconLabel = tk.Label(overarchFrame5, text="{:<39}{:<30}{:<30}".format("Bacon:",numSold["bacon"],numSold["bacon"]*prices["bacon"])).pack()
    customerServedLabel = tk.Label(overarchFrame5, text="{:<30}{:<30}".format("Customers Served:", customerServed)).pack()
    totalDaySalesLabel = tk.Label(overarchFrame5, text="{:<30}{:>0}{:<30,.2f}".format("Total Sales Before Tax","$",totalDaySales)).pack()
    totalDayTaxLabel = tk.Label(overarchFrame5, text="{:<35}{:>0}{:<30,.2f}".format("Total Tax","$",totalDayTax)).pack()
    dayTotalLabel = tk.Label(overarchFrame5, text="{:<35}{:>0}{:<30,.2f}".format("Total:","$", dayTotal)).pack()
    #Step 11.3: Allow the user to go back to the first page
    exitButton3 = tk.Button(overarchFrame5, text="Back to first page", command=backFirstPage).pack()

#Step 12: Create all the widgets for each page that were allowed to be created outside the functions (If there are widgets in functions it was to prevent bugs)
#First Page Widgets
overarchFrame = tk.Frame(window)
introLabel = tk.Label(overarchFrame, text="Please choose what the customer ordered.")
buttonFrame = tk.Frame(overarchFrame)
hamButton = tk.Button(buttonFrame, text="Hamburger", command=hamburgerToppingsPage)
friesButton = tk.Button(buttonFrame, text="Fries", command= lambda: addPrice("fries", 0))
onionButton = tk.Button(buttonFrame, text="Onion Rings", command= lambda: addPrice("onionrings",0))
smallSDButton = tk.Button(buttonFrame, text="Small Soft Drink", command= lambda: addPrice("smallsoftdrink",0))
largeSDButton = tk.Button(buttonFrame, text="Large Soft Drink", command= lambda: addPrice("largesoftdrink",0))
buttonFrame2 = tk.Frame(overarchFrame)
endOrderButton = tk.Button(buttonFrame2, text="End Order", command=lambda: endOrder(addPrice("",1)))
saleReportButton = tk.Button(buttonFrame2, text="Sales Report", command = salesReportPage)

#Hamburger Toppings Widgets
overarchFrame2 = tk.Frame(window)
buttonFrameHamburger = tk.Frame(overarchFrame2)
toppingsLabel = tk.Label(overarchFrame2, text="Please choose the toppings they want.")
cheeseTopping = tk.Button(buttonFrameHamburger, text="Cheese", command= lambda: addPrice("cheese",0))
lettuceTopping = tk.Button(buttonFrameHamburger, text="Lettuce", command= lambda: addPrice("lettuce",0))
ketchupTopping = tk.Button(buttonFrameHamburger, text="Ketchup", command= lambda: addPrice("ketchup",0))
onionTopping = tk.Button(buttonFrameHamburger, text="Onion", command= lambda: addPrice("onion",0))
tomatoTopping = tk.Button(buttonFrameHamburger, text="Tomato", command= lambda: addPrice("tomato",0))
baconTopping = tk.Button(buttonFrameHamburger, text="Bacon", command= lambda: addPrice("bacon",0))
buttonFrameHamburger2 = tk.Frame(overarchFrame2)
exitButton = tk.Button(buttonFrameHamburger2, text="Back to first page", command=backFirstPage)

#Order Page Widgets
overarchFrame3 = tk.Frame(window)
#Would have put the Subtotal, Tax, and Total After Tax down here but it just didnt work and it took me 45 minutes to debug it :(
nextCustomerButton = tk.Button(overarchFrame3, text="Next Customer", command= nextCustomerPage)

#Next Customer Page Widgets
overarchFrame4 = tk.Frame(window)
instructionLabel = tk.Label(overarchFrame4, text="Type the amount of money collected from the customer.")
amountCollected = tk.Entry(overarchFrame4)

#Sales Report Page
overarchFrame5 = tk.Frame(window)

#Step 13: Launches the first page and then starts main loop
firstPage()
window.mainloop()