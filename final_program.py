#Calvin Comstock-Fisher
#11/14/20
#Cash Register Program

import sys
import tkinter as tk

window = tk.Tk()
window.minsize(640,480)
window.title("Cash Register")

def destoryFirstPage():
    overarchFrame.destroy()

overarchFrame = tk.Frame(window)
buttonFrame = tk.Frame(overarchFrame)
hamButton = tk.Button(buttonFrame, text="Hamburger")
cheeseButton = tk.Button(buttonFrame, text="Cheese Burger")
friesButton = tk.Button(buttonFrame, text="Fries")
onionButton = tk.Button(buttonFrame, text="Onion Rings")
smallSDButton = tk.Button(buttonFrame, text="Small Soft Drink")
largeSDButton = tk.Button(buttonFrame, text="Large Soft Drink")
buttonFrame2 = tk.Frame(overarchFrame)
endOrderButton = tk.Button(buttonFrame2, text="End Order")
saleReportButton = tk.Button(buttonFrame2, text="Sales Report")
breakFrameButton = tk.Button(buttonFrame2,text="die",command=destoryFirstPage)

def firstPage():
    overarchFrame.pack()
    buttonFrame.pack(pady=5)
    hamButton.pack(side="left")
    cheeseButton.pack(side="left")
    friesButton.pack(side="left")
    onionButton.pack(side="left")
    smallSDButton.pack(side="left")
    largeSDButton.pack(side="left")
    buttonFrame2.pack()
    endOrderButton.pack(side="top")
    saleReportButton.pack(side="top")
    breakFrameButton.pack(side="bottom")

firstPage()
window.mainloop()