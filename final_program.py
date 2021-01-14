#Calvin Comstock-Fisher
#11/14/20
#Cash Register Program

import sys
import tkinter as tk

window = tk.Tk()
window.minsize(640,480)
window.title("Cash Register")

subTotal = 0
tax = 0
totalDaySales = 0
totalDayTax = 0
dayTotal = 0

def firstPage():
    overarchFrame.pack()
    buttonFrame.pack(pady=5)
    hamButton.pack(side="left")
    friesButton.pack(side="left")
    onionButton.pack(side="left")
    smallSDButton.pack(side="left")
    largeSDButton.pack(side="left")
    buttonFrame2.pack()
    endOrderButton.pack(side="top")
    saleReportButton.pack(side="top")

def backFirstPage():
    try:
        overarchFrame.destroy()
    except:
        pass
    firstPage()
    


def destoryFirstPage():
    overarchFrame.destroy()

def endOrder():
    destoryFirstPage()
    overarchFrame.pack()

def hamburgerToppingsPage():
    destoryFirstPage()
    overarchFrame.pack()
    toppingsLabel.pack()
    buttonFrame.pack()
    cheeseTopping.pack(side="left")
    lettuceTopping.pack(side="left")
    ketchupTopping.pack(side="left")
    onionTopping.pack(side="left")
    tomatoTopping.pack(side="left")
    baconTopping.pack(side="left")
    buttonFrame2.pack()
    exitButton.pack()

#First Page Widgets
overarchFrame = tk.Frame(window)
buttonFrame = tk.Frame(overarchFrame)
hamButton = tk.Button(buttonFrame, text="Hamburger", command=hamburgerToppingsPage)
friesButton = tk.Button(buttonFrame, text="Fries")
onionButton = tk.Button(buttonFrame, text="Onion Rings")
smallSDButton = tk.Button(buttonFrame, text="Small Soft Drink")
largeSDButton = tk.Button(buttonFrame, text="Large Soft Drink")
buttonFrame2 = tk.Frame(overarchFrame)
endOrderButton = tk.Button(buttonFrame2, text="End Order")
saleReportButton = tk.Button(buttonFrame2, text="Sales Report")

#Hamburger Toppings Widgets
toppingsLabel = tk.Label(overarchFrame, text="Please choose the toppings they want.")
cheeseTopping = tk.Button(buttonFrame, text="Cheese")
lettuceTopping = tk.Button(buttonFrame, text="Lettuce")
ketchupTopping = tk.Button(buttonFrame, text="Ketchup")
onionTopping = tk.Button(buttonFrame, text="Onion")
tomatoTopping = tk.Button(buttonFrame, text="Tomato")
baconTopping = tk.Button(buttonFrame, text="Bacon")
exitButton = tk.Button(buttonFrame2)



firstPage()
window.mainloop()