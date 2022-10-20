# pip Python

# Библиотека для проверки четности числа.

    from isOdd import isOdd

    print(isOdd(1))

    print(isOdd(4))

# Библиотека для визуализации процесса загрузки.

    from progress.bar import Bar

    import time

    bar = Bar('Processing', max=20)

    for i in range(20):

        time.sleep(1)

        bar.next()

        bar.finish()

# Билиотека Emoji

    import emoji

    print(emoji.emojize('Python is :thumbs_up:'))

    print(emoji.emojize("Python is fun :red_heart:"))

# Библиотека различных графиков

    import matplotlib.pyplot as plt

    import numpy as np

    list = [1, 2, 3, 4, 2, 8]

    plt.plot(list)

    plt.show()

# Telegram_Bot

## main.py

    fromtelegramimportUpdate

    fromtelegram.extimportApplicationBuilder, CommandHandler, ContextTypes

    frombot_commadsimport *

    app = ApplicationBuilder().token("5508408251:AAEMyNHOd_Ldb0O2GW6t6yyukJIhZFHlE68").build()

    app.add_handler(CommandHandler("hi", hi_command))

    app.add_handler(CommandHandler("time", time_command))

    app.add_handler(CommandHandler("sum", sum_command))

    app.add_handler(CommandHandler("help", help_command))

    print('start bot')

    app.run_polling()

## bot_commands.py

    fromtelegramimportUpdate

    fromtelegram.extimportApplicationBuilder, CommandHandler, ContextTypes

    importdatetime

    from spy import *

    asyncdefhi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

        log(update, context)

        awaitupdate.message.reply_text(f'Hi {update.effective_user.first_name}!')

    asyncdeftime_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

        log(update, context)

        awaitupdate.message.reply_text(f'{datetime.datetime.now().time()}')

    asyncdefhelp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

        log(update, context)

        awaitupdate.message.reply_text(f'/hi\n/time\n/help')

    asyncdefsum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

        log(update, context)

        msg = update.message.text

        print(msg)

        items = msg.split() # /sum 123 534543

        x = int(items[1])

        y = int(items[2])

        awaitupdate.message.reply_text(f'{x} + {y} = {x+y}')

## spy.py (Логирование)

    fromtelegramimportUpdate

    fromtelegram.extimportApplicationBuilder, CommandHandler, CallbackContext

    deflog(update: Update, context: CallbackContext):

        file = open('db.csv', 'a', encoding="utf-8")

        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')

        file.close()

