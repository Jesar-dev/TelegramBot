import telebot
from coordinates import parse_coordinates
from parce_current import parce_current
from parce_alerts import parce_alerts
from parce_daily import parce_daily
from parce_hourly import parce_hourly
import database


bot = telebot.TeleBot("1746360933:AAFY12l5eQ1mnlYHLYd9gU8c-8tVRebwrbM")


def get_coordinates(message):
    answer_town = message.text
    try:
        coordinates = parse_coordinates(answer_town)
        database.add_to_database(answer_town, coordinates)
        return coordinates
    except Exception:
        bot.send_message(message.from_user.id, "Пожалуйста напишите верный город!")
        return None


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Список команд:\n\
            /coordinates\n\
            /current_weather\n\
            /alerts\n\
            /daily_weather\n\
            /hourly_weather")
    # Проверка сообщений пользователя
    elif message.text == "/coordinates":
        msg = bot.reply_to(message, "Укажите город")
        bot.register_next_step_handler(msg, process_coordinates_step)
    elif message.text == "/current_weather":
        msg = bot.reply_to(message, "Укажите город")
        bot.register_next_step_handler(msg, process_current_step)
    elif message.text == "/alerts":
        msg = bot.reply_to(message, "Укажите город")
        bot.register_next_step_handler(msg, process_alerts_step)
    elif message.text == "/daily_weather":
        msg = bot.reply_to(message, "Укажите город")
        bot.register_next_step_handler(msg, process_daily_step)
    elif message.text == "/hourly_weather":
        msg = bot.reply_to(message, "Укажите город")
        bot.register_next_step_handler(msg, process_hourly_step)
    else:
        msg = bot.reply_to(message, "Напишите пожалуйста команду /help, \
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
