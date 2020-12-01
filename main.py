import discord
from discord.ext import commands
from config import settings
import random
from random import randint
import json
import requests
from baza import *

bot = commands.Bot(command_prefix=settings['prefix'])  # Провозглашаем переменную для бота с префиксом !


# Тут мы размещаем наши команды
@bot.command()
async def bruh(ctx):
    await ctx.send('cringe!')


@bot.command()
async def Привет(rty):
    author = rty.message.author
    await rty.send(f'Привет, {author.mention}!')


@bot.command()
async def roll(rnd, arg):
    a = int(arg)
    await rnd.send(randint(0, a))


@bot.command()
async def song(ctx):
    await ctx.send('https://www.youtube.com/watch?v=NWxISwEBU0U')  # Отправляем Embed


bot.run(settings['token'])  # Запускаем бота с вашим токеном
