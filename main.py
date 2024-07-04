import telebot
from telebot import types
from db import user,get_cashback

bot = telebot.TeleBot('7050751325:AAG6iM0ha_2001Rc9mJWfR7pHmN2M4KvROg')
zayavka_chat_id = -4243278527

btn = ['btn1','btn2','btn3','btn4']



# start начало бота
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    mar = types.KeyboardButton(text='Поделиться контактом', request_contact=True)
    markup.add(mar)
    bot.send_message(message.chat.id, text='Добро пожаловать на наш бот!', reply_markup=markup)
   
    
@bot.message_handler(content_types=['contact'])
def contact(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keshback = types.InlineKeyboardButton(text='Кэшбэк 💰')
    catalog = types.InlineKeyboardButton(text='Каталог 📁')
    last_change_oil = types.InlineKeyboardButton(text='Дата последней замены масла 📆')
    submit = types.InlineKeyboardButton(text='Оставить заявку на замены масла на дом 🛒')
    markup.add(keshback,catalog)
    markup.add(last_change_oil,submit)
    bot.send_message(message.chat.id, text=f'Вы прошли регистрацию ✅', reply_markup=markup)
    user(message.chat.id, message.contact.first_name, message.contact.phone_number)
       
    
# если получить геолокациюs
@bot.message_handler(content_types=['location'])
def location (message):
    if message.location is not None:
        bot.send_location(zayavka_chat_id, longitude=message.location.longitude, latitude=message.location.latitude)


@bot.message_handler(content_types=['text'])
def text(message):
    
    
    if message.text =='Кэшбэк 💰':
        bot.send_message(message.chat.id, text=f' ваш кэшбэк : {get_cashback(str(message.chat.id))} сум!')
    elif message.text == 'Каталог 📁':
        for i in range(1,5):
            inline_btn_1 = types.InlineKeyboardButton(f'{btn[i]}', callback_data='button1')
            inline_kb1 = types.InlineKeyboardMarkup().add(inline_btn_1)

            bot.send_message(message.chat.id, text='Text ', reply_markup=inline_kb1)

    else:
        bot.send_message(message.chat.id, text='На данный момент бот находиться на разработке !')

bot.polling(non_stop=True)