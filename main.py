# pip Python

'''
# Библиотека для проверки четности числа.

from isOdd import isOdd

print(isOdd(1))
print(isOdd(4))
'''

'''
# Библиотека для визуализации процесса загрузки.

from progress.bar import Bar
import time

bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(1)
    bar.next()
bar.finish()
'''

'''
# Билиотека Emoji

import emoji

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize("Python is fun :red_heart:"))
'''

'''
# Библиотека различных графиков

import matplotlib.pyplot as plt
import numpy as np

list = [1, 2, 3, 4, 2, 8]
plt.plot(list)

plt.show()
'''

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commads import *

app = ApplicationBuilder().token("5508408251:AAEMyNHOd_Ldb0O2GW6t6yyukJIhZFHlE68").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("help", help_command))

print('start bot')

app.run_polling()
