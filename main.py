import telebot
import buttons
from telebot import types

bot = telebot.TeleBot('6063872739:AAFMfawcps76O7J33bKSJPNksV-Cn-8x3uY')

#command /start

@bot.message_handler(commands=['start'])
def start_message(message):
    text = 'Welcome to your bot!'
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, text, reply_markup=buttons.start_buttons())

#obrabotka text messages
@bot.message_handler(content_types=['text'])
def text_message(message):
    global user_message
    user_message = message.text
    if user_message == 'Order':
        bot.send_message(user_id, 'Send your name', reply_markup=types.ReplyKeyboardMarkup)
        bot.register_next_step_handler(message, get_name)
def get_name(message, user_name):
    user_name = message.text
    bot.send_message(user_id, 'Now send your number!', reply_markup=buttons.num_buttons.num_button())
    bot.register_next_step_handler(message, get_number, user_name)
def get_number(message, user_name):
    user_number = message.contact.phone_number
    if messsage.contact:
        bot.send_message(user_id, 'Your order, what you need?', reply_markup=types.ReplyKeyboardRemove)
        #next step get order
        bot.register_next_step_handler(message, get_service, user_name)
    else:
        bot.send_message(user_id, 'Send your number through the button!')
        bot.register_next_step_handler(message, get_service, user_name, user_number)

def get_service(message, user_name, user_number):
    order_service = message.text
    bot.send_message(user_id, 'Due date>?')
    #next step get the due date
    bot.register_next_step_handler(message, get_deadline, user_name, user_number, order_service)

def get_deadline(message, user_name, user_number, user_service):
    user_deadline = message.text
    bot.send_message(-5652339702, f'new order!\n\nName: {user_name}\n'
                                  f'number: {user_number}\n'
                                  f'order: {user_service}\n'
                                  f'deadline: {user_deadline}')
    bot.send_message(user_id, 'Your order accepted, we will call you back soon')

bot.polling(none_stop=True)
