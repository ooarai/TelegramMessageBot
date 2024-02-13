import telebot

# Настройки
TOKEN = str('ТОКЕН_ВАШЕГО_БОТА')
RECEIVER_ID = int('ВАШ_АЙДИ')
IGNORED_ID = {ИГНОРИРУЕМЫЙ_АЙДИ_1, ИГНОРИРУЕМЫЙ_АЙДИ_2, И_ТАК_ДАЛЕЕ}

bot = telebot.TeleBot(TOKEN)

# /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, '<b>🎭 Для отправки сообщения используйте команду /send "сообщение". Бот поддерживает только текст, для отправки фото или видео используйте <a href="https://imgur.com/">Imgur</a> и <a href="https://www.youtube.com/">YouTube</a>.</b>', parse_mode="HTML", disable_web_page_preview = True)

# /send
@bot.message_handler(commands=['send'])
def handle_send(message):
    if message.from_user.id != RECEIVER_ID:
        if message.from_user.id not in IGNORED_ID:
            if len(message.text.split()) >= 2:
                text_to_send = ' '.join(message.text.split()[1:])
                username = message.from_user.username
                message_to_receiver = f"<b>‼️ Новое сообщение!\n\n👤 От: </b>@{username}<b> ({message.from_user.id})\n💬 Сообщение:</b> {text_to_send}"
                bot.send_message(RECEIVER_ID, message_to_receiver, parse_mode="HTML")
                bot.send_message(message.chat.id, '<b>✅ Сообщение успешно отправлено!</b>', parse_mode="HTML")
            else:
                bot.send_message(message.chat.id, '<b>❌ Вы не указали текст для отправки.</b>', parse_mode="HTML")
        else:
            bot.send_message(message.chat.id,  '<b>❌ Вы находитесь в чёрном списке и не можете отправлять сообщения.</b>', parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, '<b>❌ Вы не можете отправлять сообщения самому себе.</b>', parse_mode="HTML")

@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.send_message(message.chat.id, '<b>❌ Для просмотра доступных действий используйте команду /start.</b>', parse_mode="HTML")

bot.polling(none_stop=True)
