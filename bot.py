from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from openpyxl import load_workbook

TOKEN = '1656164530:AAF-4RoNDN6ei2TEhFHbagbJ_FNOAL26f9Y'
book = load_workbook('база данных.xlsx')
sheet_1 = book['Лист1']
schedule_page = book['расписание']


def main():
    updater = Updater(token=TOKEN)  # объект, который ловит сообщения из телеграм
    dispatcher = updater.dispatcher
    handler = MessageHandler(Filters.all, do_echo)  # отфильтровываем сообщения: теперь устройство должно реагировать
    start_handler = CommandHandler('start', do_start)
    help_handler = CommandHandler('help', do_help)
    schedule_handler = MessageHandler(Filters.all, do_sticker)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(schedule_handler)
    dispatcher.add_handler(handler)
    updater.start_polling()
    updater.idle()


def do_echo(update: Update, context):
    user = update.message.from_user.is_bot
    name = update.message.from_user.first_name
    if user:
        update.message.reply_text(text=f"Ты - бот! Уходи отсюда!!!")
    else:
        update.message.reply_text(text=f"ААААА! {name} что ты делаешь?")



    if text == "привет":
        update.message.reply_text(text="доброго времени суток, друг", reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text(text="Привет! Нажми /start чтобы запустить меня:)", reply_markup=ReplyKeyboardRemove())



def do_start(update, context):
    keyboard = [
        ["понедельник", "вторник", "среда", "четверг", "пятница"]
    ]
    update.message.reply_text(
        text="Выбери день чтобы узнать расписание",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True))


def do_help(update, context):
    update.message.reply_text(text="что случилось? Всё ж было норм")



def do_sticker(update: Update, context):
    sticker_id = update.message.sticker.file_id
    update.message.reply_text(sticker_id)
    update.message.reply_sticker(sticker_id)


def do_something(update, context):
    text = update.message.text

    print(stickers_page.max_row)
    for row in range(2, stickers_page.max_row + 1):
        catch_phrase = stickers_page.cell(row=row, column=4).value
        print(catch_phrase)
        print(text)
        if catch_phrase in text:
            sticker_id = stickers_page.cell(row=row, column=3).value
            update.message.reply_sticker(sticker_id)





main()