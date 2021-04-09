# bot.py
import os

import random
import discord
import datetime

TOKEN = 'ODE3MTQ0NjE1NTE3NTUyNjQx.YEFPOg.qy2oHzimBQzqaLEuQIjBRMbnxB8'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

dagar = ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'abrakadabra!':
        for x in range(1, 8):
            date = datetime.date.today() + datetime.timedelta(days=x)
            veckodag = dagar[int(date.strftime("%w"))]
            datum = date.strftime("%d")
            manad = date.strftime("%m")
            response = veckodag + " " + datum + "/" + manad
            await message.channel.send(response)
            

client.run(TOKEN)
