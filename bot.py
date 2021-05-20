import os
import telebot
import database
from coordinates import parse_coordinates
from parce_alerts import parce_alerts
from parce_current import parce_current
from parce_daily import parce_daily
from parce_hourly import parce_hourly


bot = telebot.TeleBot(os.environ.get('APIBOT'))


def get_coordinates(message):
    answer_town = message.text
    try:
        coordinates = parse_coordinates(answer_town)
        database.add_to_database(answer_town, coordinates)
        return coordinates
    except Exception:
        bot.send_message(message.from_user.id, "Пожалуйста напишите верный город!")
        return None


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.from_user.id, "Список команд:\n\
        /coordinates\n\
        /current_weather\n\
        /alerts\n\
        /daily_weather\n\
        /hourly_weather")
    # Проверка сообщений пользователя


@bot.message_handler(commands=['coordinates'])
def coord_commnand(message):
    msg = bot.reply_to(message, "Укажите город")
    bot.register_next_step_handler(msg, process_coordinates_step)


@bot.message_handler(commands=['current_weather'])
def current_command(message):
    msg = bot.reply_to(message, "Укажите город")
    bot.register_next_step_handler(msg, process_current_step)


@bot.message_handler(commands=['alerts'])
def alert_command(message):
    msg = bot.reply_to(message, "Укажите город")
    bot.register_next_step_handler(msg, process_alerts_step)


@bot.message_handler(commands=['daily_weather'])
def daily_commmand(message):
    msg = bot.reply_to(message, "Укажите город")
    bot.register_next_step_handler(msg, process_daily_step)


@bot.message_handler(commands=['hourly_weather'])
def hourly_command(message):
    msg = bot.reply_to(message, "Укажите город")
    bot.register_next_step_handler(msg, process_hourly_step)


@bot.message_handler(content_types=['text'])
def other_commands(message):
    bot.reply_to(message, "Напишите пожалуйста команду /help, \
чтобы узнать список команд")


def process_coordinates_step(message):
    answer_town = message.text
    if (database.check_database(answer_town)):
        coordinates = database.get_coordinates_from_database(answer_town)
    else:
        coordinates = get_coordinates(message)
    if coordinates is not None:
        bot.send_message(message.from_user.id, "Координаты: \
{0}".format(coordinates))


def process_current_step(message):
    answer_town = message.text
    if (database.check_database(answer_town)):
        coordinates = database.get_coordinates_from_database(answer_town)
    else:
        coordinates = get_coordinates(message)
    if coordinates is not None:
        result = parce_current(coordinates)
        bot.send_message(message.from_user.id, result)


def process_alerts_step(message):
    answer_town = message.text
    if (database.check_database(answer_town)):
        coordinates = database.get_coordinates_from_database(answer_town)
    else:
        coordinates = get_coordinates(message)
    if coordinates is not None:
        result = parce_alerts(coordinates)
        bot.send_message(message.from_user.id, result)


def process_daily_step(message):
    answer_town = message.text
    if (database.check_database(answer_town)):
        coordinates = database.get_coordinates_from_database(answer_town)
    else:
        coordinates = get_coordinates(message)
    if coordinates is not None:
        result = parce_daily(coordinates)
        bot.send_message(message.from_user.id, result)


def process_hourly_step(message):
    answer_town = message.text
    if (database.check_database(answer_town)):
        coordinates = database.get_coordinates_from_database(answer_town)
    else:
        coordinates = get_coordinates(message)
    if coordinates is not None:
        result = parce_hourly(coordinates)
        bot.send_message(message.from_user.id, result)


bot.polling(none_stop=True, interval=0)
