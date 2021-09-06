import telebot
from telebot import types
import json
from random import choice


TOKEN = '1976058494:AAFJ00bUPnBF9scI2CPTcv_TV1sH7X9u6II'

bot = telebot.TeleBot(TOKEN)


def gen_markup():
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Первое')
    itembtn2 = types.KeyboardButton('Второе')
    itembtn3 = types.KeyboardButton('Десерт')
    markup.add(itembtn1, itembtn2, itembtn3)
    return markup


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    with open("recipes.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    
    recipes = data.get(message.text)

    if recipes is None:
        bot.send_message(message.chat.id, "Нажми на кнопку с видом блюда", reply_markup=gen_markup())
    else:
        recipe = choice(recipes)
        meal_name = recipe["meal_name"]
        meal_src = "https://www.russianfood.com/recipes/recipe.php?rid="
        meal_id = recipe["meal_id"]
        bot.send_message(message.chat.id, meal_name + "\n" + meal_src + meal_id, reply_markup=gen_markup())

bot.polling(none_stop=True)
