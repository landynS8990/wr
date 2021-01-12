import random
from tkinter import *
import tkinter
from cardo import Cards, Decks
import asyncio
import logging
import threading
import time
from PIL import Image, ImageTk


class Card:
    #Create card class
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    RANKS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King')
    #Suit and rank dicts

    def __init__(self, suit=0, rank=0):
        #Define init method
        self.suit = suit
        #Self.suit is equal to suit
        self.rank = rank
        #Self.rank is equal to rank
    #endmthod
    def __str__(self):
        #Define str method
        return '{0} of {1}'.format(Card.RANKS[self.rank],
                                   Card.SUITS[self.suit])
        #Return suit and rank as a string
    #endmethod
#endclass


class Deck:
    #Create deck class
    def __init__(self):
        #Define init method
        self.cards = []
        #Define a list of cards
        for suit in range(4):
            #Loop through suit
            for rank in range(1, 14):
                #Loop through ranks
                self.cards.append(Card(suit, rank))
                #Append each suit and rank to card list
            #endfor
        #endfor
    #endmethod
    def print_deck(self):
        #Define print deck method
        for card in self.cards:
            #Loop through card list
            print(card)
            #Print each index
        #endfor
    #endmethod
    def remove(self, card):
        #Define remove method
        if card in self.cards:
            #loop through card list
            self.cards.remove(card)
            #Remove card list at argument 1 index
            return True
            #Return true
        else:
            #if item not in list
            return False
            #Return false
        #endif
    #endmethod
    def shuffle(self):
        num_cards = len(self.cards)
        #Define length of card list
        for i in range(num_cards):
            #Loop through card list
            j = random.randrange(i, num_cards)
            #get random item from list
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
            #Insert into current index
        #endfor
    #endmethod

    def returnList(self):
        #Define returnList function
        s = []
        #Define s as 0
        for i in range(len(self.cards)):
            #Loop through card list
            s += [str(self.cards[i])]
            #Add current index to s
        #endfor
        return s
        #return s
    #endmethod

    def __str__(self):
        #Define str method
        s = ""
        #Define s as empty list
        for i in range(len(self.cards)):
            #Loop through card list
            print(str(self.cards[i]))
            #print current index
        return s
        #Return s
    #endmethod
#endclass


def onlyNumbs(arr):
    #Define onlyNumbs function
    powerList = ["Jack", "King", "Queen", "Ace"]
    #Define list of suits
    numbList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #Define list of numbers
    t = list(arr)
    #get input string as list
    r = ""
    #Define r as empty string
    for i in t:
        #Loop through input string
        if i in numbList:
            #If teh current index is in the number lisr
            r += i
            #Add i it r
        #endif
    #endfor
    y = 0
    #Define y as 0
    while y < len(powerList):
        #Loop though list of suits
        if powerList[y] in arr:
            #Uf rge current index is in the input string
            r = str(y + 10)
            #Add y + 10 to r
        #endif
        y += 1
        #Add 1 to y
    #endwhi;e
    return r
    #Return r
#endfunction

def getFileName(name):
    #Define getFileName function
    uArr = name.split(" of ")
    #Split name string into suit and rank
    rn = Card().RANKS
    #Get card ranks
    numVar = 0
    #Define numVar as 0
    u = 0
    #Define u as 0
    for i in rn:
        #Loop through ranks
        if i == uArr[0]:
            #If the current index is equal to the input card's rank
            numVar = u
            #Define numVar as u
        #endif
        u += 1
        #Add 1 to u
    #endfor

    strVar = ""
    #Define strWar as 0
    if uArr[1] == "Clubs":
        #if the card's suit is clubs
        strVar = "c"
        #StrVar is c
    elif uArr[1] == "Spades":
        #If the card's suit is spades
        strVar = "s"
        #strVar is s
    elif uArr[1] == "Hearts":
        #If the card's suit is hearts
        strVar = "h"
        #strVar is h
    elif uArr[1] == "Diamonds":
        #if the card's suit is diamonds
        strVar = "d"
        #strVar is d
    #endif
    manStr = "DECK/" + str(numVar) + strVar + ".gif"
    #Format the string to match the gif files
    return manStr
    #return manStr
#endmethod




class showStuff:
    #Define showStuff class


    def __init__(self):
        #Define init method

        print("Welcome to war. Each turn, you and your opponent will draw a card and whoever's card is greater wins. The game continues until a player is out of cards.")
        #Print message to user
        self.deck = Deck()
        #Define self.deck as Deck() object
        self.deck.shuffle()
        #Shuffle deck
        self.d = self.deck.returnList()
        #Return list of cards
        self.player1 = []
        #Define player 1 list
        self.player2 = []
        #Define player 2 list
        self.t = int(len(self.d) / 2)
        #Split card list in half
        i = 0
        #Define i as 0
        while i < len(self.d):
            #While i is less than half of 2
            if i < 26:
                self.player1 += [self.d[i]]
            else:
                self.player2 += [self.d[i]]
            #Give half of the list to player1, the other half to player2
            #endif
            i += 1
            #Add 1 to i
        #endwhile

        self.root = Tk()
        self.root.geometry("600x400")
        #Create tkinter window
        self.B = tkinter.Button(self.root, text ="Next hand", command = self.playDef)
        self.B.pack()
        #Create button and make it call to the playDef method

        self.H = tkinter.Button(self.root, text ="Instructions", command = self.instr)
        self.H.place(relx = 100, rely = 200, anchor = 'sw')
        self.H.pack()
        #Create button and make it call to the instr method

        self.Q = tkinter.Button(self.root, text ="Quit game", command = self.root.destroy)
        self.Q.pack()
        #Create button and make it destroy the tkinter window

        self.var = StringVar()
        self.label = Label( self.root, textvariable=self.var, relief=RAISED )
        self.var.set("Your score: ")
        self.label.pack()
        #Create label for player's score

        self.var2 = StringVar()
        self.label2 = Label( self.root, textvariable=self.var2, relief=RAISED )
        self.var2.set("Computer score: ")
        self.label2.pack()
        #Create label for computer score

        self.var3 = StringVar()
        self.label3 = Label( self.root, textvariable=self.var3)
        self.var3.set("")
        self.label3.pack()
        #Create label for winner of each hand

        self.var4 = StringVar()
        self.labels4 = Label( self.root, textvariable=self.var4, pady=15, width=105)
        self.var4.set("")
        self.labels4.pack()
        #Create label for instructions paragraph

        self.root.mainloop()
        #Run mainLoop()
    #endinit

    def instr(self):
        #Define instr() as method
        self.var.set("")
        self.var2.set("")
        self.var3.set("")
        #Set the user messages to blank to clear the page
        self.playerWar("DECK/blanks.gif", "DECK/blanks.gif", "DECK/blanks.gif", "DECK/blanks.gif", "DECK/blanks.gif")
        self.cpuWar("DECK/blanks.gif", "DECK/blanks.gif", "DECK/blanks.gif", "DECK/blanks.gif", "DECK/blanks.gif")
        #Turn all cards into white squares
        self.var4.set("The deck is split between you and the computer \nat the beginning of every game. When you click next hand \na card is drawn from yours and your opponent's decks. \nWhoever has the greater wins the hand and is awarded both cards in play. \nWhoever's deck is larger by the end wins. ")
        #Set text in label to print instructions to user
    #endmethod
    def playerWar(self, nm1, nm2, nm3, nm4, nm5):
        #Define playerWar as method
        self.images0 = Image.open(nm1)
        self.tests0 = ImageTk.PhotoImage(self.images0)
        #Get image file from first argument
        self.labele0 = tkinter.Label(image=self.tests0)
        self.labele0.image = self.tests0
        #Create tkinter label
        self.labele0.place(x=30, y=40)
        #Set position in window
        self.images1 = Image.open(nm2)
        self.tests1 = ImageTk.PhotoImage(self.images1)
        #Get image file from second argument
        self.labele1 = tkinter.Label(image=self.tests1)
        self.labele1.image = self.tests1
        #Create tkinter label
        self.labele1.place(x=150, y=40)
        #Set position in window
        self.images2 = Image.open(nm3)
        self.tests2 = ImageTk.PhotoImage(self.images2)
        #Get image file from third argument
        self.labele2 = tkinter.Label(image=self.tests2)
        self.labele2.image = self.tests2
        #Create tkinter label
        self.labele2.place(x=350, y=40)
        #Set position in window
        self.images3 = Image.open(nm4)
        self.tests3 = ImageTk.PhotoImage(self.images3)
        #Get image file from fourth argument
        self.labele3 = tkinter.Label(image=self.tests3)
        self.labele3.image = self.tests3
        #Create tkinter label
        self.labele3.place(x=430, y=40)
        #Set position in window
        self.images4 = Image.open(nm5)
        self.tests4 = ImageTk.PhotoImage(self.images4)
        #Get image file from fifth argument
        self.labele4 = tkinter.Label(image=self.tests4)
        self.labele4.image = self.tests4
        #Create tkinter label
        self.labele4.place(x=520, y=40)
        #Set position in window
    #endmethod
    def cpuWar(self, nm1, nm2, nm3, nm4, nm5):
        #Define cpuWar as method
        self.images0 = Image.open(nm1)
        self.tests0 = ImageTk.PhotoImage(self.images0)
        #Get image file from first argument
        self.labele0 = tkinter.Label(image=self.tests0)
        self.labele0.image = self.tests0
        #Create tkinter label
        self.labele0.place(x=30, y=250)
        #Set position underneath user cards
        self.images1 = Image.open(nm2)
        self.tests1 = ImageTk.PhotoImage(self.images1)
        #Get image file from second argument
        self.labele1 = tkinter.Label(image=self.tests1)
        self.labele1.image = self.tests1
        #Create tkinter label
        self.labele1.place(x=150, y=250)
        #Set position in window
        self.images2 = Image.open(nm3)
        self.tests2 = ImageTk.PhotoImage(self.images2)
        #Get image file from third argument
        self.labele2 = tkinter.Label(image=self.tests2)
        self.labele2.image = self.tests2
        #Create tkinter label
        self.labele2.place(x=350, y=250)
        #Set position in window
        self.images3 = Image.open(nm4)
        self.tests3 = ImageTk.PhotoImage(self.images3)
        #Get image file from fourth argument
        self.labele3 = tkinter.Label(image=self.tests3)
        self.labele3.image = self.tests3
        #Create tkinter label
        self.labele3.place(x=430, y=250)
        #Set position in window
        self.images4 = Image.open(nm5)
        self.tests4 = ImageTk.PhotoImage(self.images4)
        #Get image file from fifth argument
        self.labele4 = tkinter.Label(image=self.tests4)
        self.labele4.image = self.tests4
        #Create tkinter label
        self.labele4.place(x=520, y=250)
        #Set position in window
    #endmethod


    def playDef(self):
        #Define playDef method
        pl1 = self.player1.pop()
        pl2 = self.player2.pop()
        #Get single card from player1 and player2's decks
        self.playerWar("DECK/blanks.gif", "DECK/b.gif", getFileName(pl1), "DECK/blanks.gif", "DECK/blanks.gif")
        self.cpuWar("DECK/blanks.gif", "DECK/b.gif", getFileName(pl2), "DECK/blanks.gif", "DECK/blanks.gif")
        #Display single cards with the playWar function and substitute all other cards for blank spaces
        self.var.set("Your score: " + str(len(self.player1)))
        self.var2.set("Cpu score: " + str(len(self.player2)))
        #Get the length of the player1 and player2 lists and display them to the user to show their score
        self.B.config(text="Next hand")
        self.H.config(text="Instructions")
        self.Q.config(text="Quit game")
        #Make sure buttons have correct text
        self.var4.set("")
        #Make sure instructions aren't still being shown
        p1 = int(onlyNumbs(pl1))
        p2 = int(onlyNumbs(pl2))
        #Get the numerical value of each player's hand
        if p1 > p2:
            #If player1's hand is greater
            print("You win")
            self.player1.insert(0, pl1)
            self.player1.insert(0, pl2)
            #Add both player1 and player2's cards to player1's list
            self.var3.set(f"{pl1} beats {pl2}. You win")
            #Display message to user
        elif p2 > p1:
            #If player2's hand is greater
            print("Your opponent wins")
            #Print message to user
            self.player2.insert(0, pl1)
            self.player2.insert(0, pl2)
            #Add both player1 and player2's cards to player2's list
            self.var3.set(f"{pl2} beats {pl1}. Computer wins")
            #Display message to user
        else:
            print("You and your opponent have the same card. ")
            #Print message to user
            warList1 = []
            warList2 = []
            #Definen warLists 1 and 2 as empty lists
            y = 0
            b1 = self.player1.pop()
            b2 = self.player1.pop()
            b3 = self.player1.pop()
            b4 = self.player1.pop()
            b5 = self.player1.pop()
            b6 = self.player1.pop()
            b7 = self.player1.pop()
            b8 = self.player1.pop()
            b9 = self.player1.pop()
            b0 = self.player1.pop()
            #Pop 5 cards from player1 and player2's decks respectively
            p1List = [pl1, b2, b3, b4, b5]
            p2List = [pl2, b7, b8, b9, b0]
            #Add popped cards to player lists
            self.playerWar(getFileName(pl1), getFileName(b2), getFileName(b3), getFileName(b4), getFileName(b5))
            self.cpuWar(getFileName(pl2), getFileName(b7), getFileName(b8), getFileName(b9), getFileName(b0))
            #Display popped cards on screen
            for i in p1List:
                #Loop through p1List
                warList1.append(int(onlyNumbs(i)))
                #Append number value of i to warList1
            #endfor
            for d in p2List:
                #Loop through p2List
                warList2.append(int(onlyNumbs(d)))
                #Append number value of i to warList2
            #endfor
            print(f"You have {warList1}")
            print(f"Your opponent has {warList2}")
            #Print message to user
            if sum(warList1) > sum(warList2):
                #If the sum of warList 1 is greater than that of warList2
                print("You win")
                #Print message
                for i in p1List:
                    #Loop through p1List
                    self.player1.append(i)
                    #Append each value to player1's list
                #endfor
                for t in p2List:
                    #Loop through p2List
                    self.player1.append(t)
                    #Append each value to player2's list
                #endfor
                self.var3.set(f"Your list beats your opponent's list. You win")
                #Display message to user
            elif sum(warList2) > sum(warList1):
                #If the sum of warList2 is greater than that of warList1
                print("Your opponent wins")
                #Print message to user
                for i in p2List:
                    #Loop through p2List
                    self.player2.append(i)
                    #Append each card to player2's list
                #endfor
                for t in p1List:
                    #Loop through p1List
                    self.player2.append(t)
                    #Append each card to player2's list
                #endfor
                self.var3.set(f"Your opponent's list beats yours. You lose")
                #Display message to user
            else:
                #If they're the same
                print("Draw")
                #Print message to user
                for i in p1List:
                    self.player1.append(i)
                for t in p2List:
                    self.player2.append(t)
                #Divide the cards im play equally among the two players


def play():
    #Define play() function
    g = showStuff()
    #Instantiate showStuff() class and run main loop

play()
#Call to play() function
