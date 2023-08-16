from telebot import types

#buttons in start
def start_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #creating buttons
    order_button = types.KeyboardButton('Order')
    #add buttons in place
    kb.add(order_button)
    #return place
    return kb
def new_button():
    #place for buttons
    kb = types.ReplyKeyboardMakup(resize_keyboard=true)
    #create buttons
    number_button = types.KeyBoardbutton('Send your number', request_contact=True)
    #add button to place
    kb.add(number_button)
    #return to place
    return kb