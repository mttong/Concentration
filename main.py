from tkinter import *
from card import Card
import random

#create buttons and display onto screen
def make_buttons(deck):
    global list_of_buttons

    for r in range(4):
        for c in range(13):
            #making individual frame for each button
            frame = Frame(master=concentration, relief=RAISED, borderwidth=1)
            #gridding each frame
            frame.grid(row=r, column=c)

            #if card is a heart or diamond, will display text of button as red
            if deck[c][r].suit == "♦" or deck[c][r].suit == "♥":
                list_of_buttons[c][r] = Button(master=frame, text=' ', fg='red',
                                    font=("Arial", 20), height=3, width=3,
                                command= lambda r=r, c=c: flip_card(list_of_buttons[c][r], deck[c][r]))

            #if card is spade or clubs, will display text of button as black
            else:
                list_of_buttons[c][r] = Button(master=frame, text=' ',
                                    font=("Arial", 20), height=3, width=3,
                                command= lambda r=r, c=c: flip_card(list_of_buttons[c][r], deck[c][r]))

            list_of_buttons[c][r].pack(padx = 3, pady = 3)

#command called when buttons are clicked
def flip_card(button, card):
    global temp_cards, temp_cards_dict

    #checks if text is black first
    if button['text'] == ' ':
        #displays card
        button['text'] = f'{card}'

        #adds card to temp_cards
        temp_cards.append(card)
        #adds button and card to temp_cards_dict {key: button, value: card}
        temp_cards_dict[button] = card

    #checks once temp_cards has at least two cards in it
    if len(temp_cards) > 2:
        #comparing cards
        check_cards()

#compares cards in temp_cards, temp_cards_dict to see if they match
def check_cards():
    global temp_cards, temp_cards_dict, score

    #checks if first two items of temp_cards are equal
    if temp_cards[0] == temp_cards[1]:
        #creates a list of the buttons currently in temp_cards_dict
        key_list = list(temp_cards_dict.keys())

        #disables the first two buttons in the list
        for button in key_list[:2]:
            button['state'] = 'disabled'
        #turns the third one back to blank
        for button in key_list[2:]:
            button['text'] = ' '

        #resets dictionary and list
        temp_cards_dict = {}
        temp_cards = []

        #decrements score and displays
        score -= 1
        score_label = Label(concentration, text=('Pairs Left: ', score))
        score_label.place(relx=1.0, rely=0.0, anchor='ne')

        #checking if win
        if score == 1:
            win()

    #if cards are not equal
    else:
        #flips them back down
        for button in temp_cards_dict:
            button['text'] = ' '

        #resets dictionary and list
        temp_cards = []
        temp_cards_dict = {}

#win function
def win():
    global list_of_buttons, deckOfCards

    #creates new window
    win = Toplevel()
    win_label = Label(win, text='You Win!!').pack()

    #disables all buttons, flips the remaining and colors them all magenta
    for r in range(4):
        for c in range(13):
            button = list_of_buttons[c][r]
            button['text'] = deckOfCards[c][r]
            button['state'] = 'disabled'
            button.config(bg='magenta')

    #showing score label as 0
    score_label = Label(concentration, text=('Pairs Left: 0'))
    score_label.place(relx=1.0, rely=0.0, anchor='ne')

if __name__ == '__main__':
    # setting the window
    concentration = Tk()
    concentration.wm_title('Concentration')

    """
    global variables:
        temp_cards_dict = keeps track of clicked buttons, stores button and card 
        temp_cards = keeps track of cards clicked on 
        list_of_buttons = stores all the buttons as a matrix to get coordinate 
        score = how many pairs left 
    """
    temp_cards_dict = {}
    temp_cards = []
    list_of_buttons = [[0] * 4 for r in range(13)]
    score = 26

    #creating deck
    deck = []
    for suit in Card.SUITS:
        for rank in Card.RANK:
            deck.append(Card(suit, rank))
    #shuffling
    random.shuffle(deck)

    #putting deck into matrix to grid
    counter = 0
    deckOfCards = [[0] * 4 for r in range(13)]
    for r in range(4):
        for c in range(13):
            deckOfCards[c][r] = (deck[counter])
            counter += 1

    #calling make_buttons function
    make_buttons(deckOfCards)


    #run tkinter event loop
    concentration.mainloop()
