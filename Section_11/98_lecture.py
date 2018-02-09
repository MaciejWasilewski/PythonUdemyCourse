import random
import tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    for suit in suits:
        for card in range(1, 11):
            name = "cards/{0}_{1}.{2}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
        for card in face_cards:
            name = "cards/{0}_{1}.{2}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


mainWindow = tkinter.Tk()

mainWindow.title("Black Jack")
mainWindow.geometry("640x480")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

dealer_button = tkinter.Button(button_frame, text="Dealer")
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player")
player_button.grid(row=0, column=1)

cards = []
load_images(cards)

deck = list(cards)
random.shuffle(deck)

dealer_hand = []
player_hand = []

mainWindow.mainloop()
