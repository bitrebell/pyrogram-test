from pyrogram import Client, filters


bot = Client(
    "this is testing era",
    api_id= 10738943,
    api_hash= "da61e3a08b5ac78ce28b4a4cd854aeec",
    bot_token = "6412441114:AAF5nri-Vw1kcwvMn4JT4KzXH2Fjpxv3HHA"

)


#Send Message 
@bot.on_message(filters.command('start') & filters.private)
def start (bot, message):
    bot.send_message(message.chat.id, "Hiii this is your aka bhai......please coprate ")


#REply Message 
@bot.on_message(filters.command('help'))
def help (bot, message):
    message.reply_text("hiii")

#Welcome Bot

GROUP = "testingg_groupp"
WELCOME_MESSAGE = "Heloo Welcome To Group Chat!"

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(Client, message):
    message.reply_text(WELCOME_MESSAGE)

#Send Photo
@bot.on_message(filters.command('photo'))
def photo (bot, messaage):
    bot.send_photo(messaage.chat.id, "https://docs.pyrogram.org/_static/pyrogram.png")

#TO get id of video/audio/sticker/animation/voice

@bot.on_message(filters.document & filters.private)
def document(bot, message):
    message.reply(message.document.file_id)

#Send Audio/Documents/Sticker/Video/Animation/Voice

@bot.on_message(filters.command('video'))
def video (bot, messaage):
    bot.send_video(messaage.chat.id, "link")

@bot.on_message(filters.command('audio'))
def audio (bot, messaage):
    bot.send_audio(messaage.chat.id, "link")


#Delete message

@bot.on_message(filters.text)
def delete_text (bot, message):

    word_list =["fuck", "bc", "mc"]

    if message.text in word_list:
        bot.delete_messages(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "NIKAL LAWDE")






print("I AM ALIVE")
bot.run()