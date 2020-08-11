import telepot

bot = telepot.Bot("1374083089:AAHei2vT_Yprz_gZr5da5PfkX19nAZWl2_c")

def recebendoMsg(msg):
    print(msg['text'])

bot.message_loop(recebendoMsg)

while True:
    pass
