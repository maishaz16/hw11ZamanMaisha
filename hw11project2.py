# Exercise No.   2
# File Name:     hw11project2.py
# Programmer:    Maisha Zaman
# Date:          July 25, 2020
#
# Problem Statement: Create a GUI with a text box, button and a picture.
# The user will type in the suit of a card (spade, clubs, hearts, diamond)
# and it will show the corresponding suit.  Use a dictionary as the
# storage mechanism.
#
# Overall Plan:
# 1. Import graphics and button
# 2. Print Code Introduction
# 3. Draw GUI window
# 4. Design interface, i.e entry box, text, image placement
# 5. Design images of cards
# 6. Have buttons activate/deactivate when clicked
# 7. Display image depending on what is clicked

from graphics import *
from button import Button

def hw11project11():

    ## Print code introduction
    print("This code will show you a the suit of a card")

    ## create the application window
    win = GraphWin("Card Suit Displayer", 500,500)
    win.setCoords(0.0, 0.0, 5.0, 5.0)
    win.setBackground("Lavender")

    ## Format GUI
    # Display Text in window
    Text(Point(2.5, 1.5), "Enter the type of suit to be displayed (spades, "
                          "clubs, hearts, diamonds): "
                          "").draw(win)

    # Add entry for user to input suit type
    input = Entry(Point(2.5, 1.15), 10)
    input.setText("")
    input.draw(win)

    # Create buttons and activate
    display = Button(win, Point(1.5, .5), 1, .45, 'Display')
    display.activate()
    quit = Button(win, Point(3.5, .5), 1, .45, 'Quit')
    quit.activate()

    ## Store image files of each card type
    image_center = Point(2.5,3.25)
    hearts = Image(image_center, "hearts.png")
    spades = Image(image_center, "spades.png")
    diamonds = Image(image_center, "diamonds.png")
    clubs = Image(image_center, "clubs.png")


    ## Activating loop depending on which button is clicked

    # define mouse click as a point
    pt = win.getMouse()
    # run code if the quit button is not clicked
    while not quit.clicked(pt):
        # enter inputs and allow convert button to initiate calculations
        if display.clicked(pt):
            # Store inputted text
            text = input.getText()

            # display card depending on what is typed in
            if text == "hearts" or text == "heart":
                hearts.draw(win)
            elif text == "spades" or text == "spade":
                spades.draw(win)
            elif text == "diamonds" or text == "diamond":
                diamonds.draw(win)
            elif text == "clubs" or text == "club":
                clubs.draw(win)
            # display error message if none of the suits are typed in correctly
            else:
                Text(image_center,"Error. Please Quit and Try Again").draw(win)
            display.deactivate()

        # continue while loop to make sure all clicks are not hitting quit
        pt = win.getMouse()

    # Close Window
    win.close()

hw11project11()

