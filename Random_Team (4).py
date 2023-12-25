import telebot
from telebot import types
import openai
from kandinsky import kandinsky_ai
from yandex_gpt import yandex_ai


bot = telebot.TeleBot('6933111743:AAEQLDP9iPptPfDGeicu5HUc_jb331Eipy8')
Chat_GPT = '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'
openai.api_key = Chat_GPT

def GPT(message):
    response = openai.Completion.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = message,
        temperature = 0.5,
        max_tokens = 1000,
        top_p = 1.0,
        frequency_penalty = 0.5,
        presence_penalty = 0.5
        )
    gpt_text = response['choices'][0]['text']
    return gpt_text

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('/Chat_GPT')
    btn2 = types.KeyboardButton('/Kandinsky')
    btn3 = types.KeyboardButton('/Yandex_GPT')
    btn4 = types.KeyboardButton('Обучение')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, '''
Привет!
Наш бот предоставляет вам возможность получить ответ на
интересующий вас вопрос. Но будьте внимательны и всегда
перепроверяйте получаемую информацию, ИИ иногда может
ошибаться.
        ''', reply_markup = markup)


def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('/Chat_GPT')
    btn2 = types.KeyboardButton('/Kandinsky')
    btn3 = types.KeyboardButton('/Yandex_GPT')
    btn4 = types.KeyboardButton('Обучение')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text = 'Вы вернулись в главное меню', reply_markup = markup)


#YANDEX GPT
@bot.message_handler(commands = ['Yandex_GPT'])
def yandex_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Вернуться в главное меню')
    markup.add(btn1)
    mesg_yandex = bot.send_message(message.chat.id, text = '''
Вы можете говорить с YandexGPT
Пожалуйста, ждите 20 секунд перед тем как отправлять
следующее сообщение
        ''', reply_markup = markup)
    bot.register_next_step_handler(mesg_yandex, yandex_2)

def yandex_2(message):
    if (message.text) == 'Вернуться в главное меню':
        return back(message)
    answer_yandex = yandex_ai(message.text)
    bot.register_next_step_handler(message, yandex_2)
    if answer_yandex != False:
        bot.send_message(message.chat.id, answer_yandex)
    else:
        bot.send_message(message.chat.id, 'Ошибка сервера')
        return yandex_1(message)
#CHAT GPT
@bot.message_handler(commands = ['Chat_GPT'])
def GPT_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Вернуться в главное меню')
    markup.add(btn1)
    mesg_GPT = bot.send_message(message.chat.id, text = '''
Вы можете говорить с  ChatGPT
Пожалуйста, ждите 20 секунд перед тем как отправлять
следующее сообщение
        ''', reply_markup = markup)
    bot.register_next_step_handler(mesg_GPT, GPT_2)

def GPT_2(message):
    if (message.text) == 'Вернуться в главное меню':
        return back(message)
    answer_GPT = GPT(message.text)
    bot.register_next_step_handler(message, GPT_2)
    if answer_GPT != False:
        bot.send_message(message.chat.id, answer_GPT)
    else:
        bot.send_message(message.chat.id, 'Ошибка сервера')
        return GPT_2(message)


#KANDINSKY
@bot.message_handler(commands = ['Kandinsky'])
def kandinsky_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Вернуться в главное меню')
    markup.add(btn1)
    mesg_kandinsky = bot.send_message(message.chat.id, text = '''
Вы выбрали Kadinskiy. Для использования пропишите слово,
которые вы хотите визуализировать, без использования
каких либо дополнительных команд.
Пример : "Яблоко"/"Apple"
        ''', reply_markup = markup)
    bot.register_next_step_handler(mesg_kandinsky, kandinsky_2)

def kandinsky_2(message):
    if (message.text) == 'Вернуться в главное меню':
        return back(message)
    answer_kandinsky = kandinsky_ai(message.text, message.from_user.id)
    bot.register_next_step_handler(message, kandinsky_2)
    if answer_kandinsky != False:
        img = open(answer_kandinsky, 'rb')
        bot.send_photo(message.chat.id, img)
    else:
        bot.send_message(message.chat.id, 'Ошибка сервера')



#УЧЕБНЫЙ МОДУЛЬ
@bot.message_handler(commands=['Модуль_1'])
def module_1(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Модуль 1", url = 'http://testmodule.tilda.ws/test1')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['Модуль_2'])
def module_2(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Модуль 2", url = 'http://testmodule.tilda.ws/test2')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['Модуль_3'])
def module_3(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Модуль 3", url = 'http://testmodule.tilda.ws/test3')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def education(message):
    if (message.text) == 'Обучение':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn1 = types.KeyboardButton('/Модуль_1')
        btn2 = types.KeyboardButton('/Модуль_2')
        btn3 = types.KeyboardButton('/Модуль_3')
        btn4 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, '''
Добро пожаловать в наш обучающий модуль
Выберете один из модулей по кнопке ниже
            ''', reply_markup = markup)

    elif (message.text) == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn1 = types.KeyboardButton('/Chat_GPT')
        btn2 = types.KeyboardButton('/Kandinsky')
        btn3 = types.KeyboardButton('/Yandex_GPT')
        btn4 = types.KeyboardButton('Обучение')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text = 'Вы вернулись в главное меню', reply_markup = markup)

    elif (message.text) == 'Вернуться к модулям':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn1 = types.KeyboardButton('/Модуль_1')
        btn2 = types.KeyboardButton('/Модуль_2')
        btn3 = types.KeyboardButton('/Модуль_3')
        btn4 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text = 'Вы вернулись назад', reply_markup = markup)



bot.polling(none_stop = True)