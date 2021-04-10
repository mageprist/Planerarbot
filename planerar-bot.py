# bot.py
import os

import random
import discord
import datetime
from discord.ext import commands

with open('token.txt', 'r') as file: #läser in TOKEN från token.txt (underlättar vid git).
    TOKEN = file.read()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

dagar = ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag"]
emoji_yes = '☑️'
emoji_no = '❌'

msg_set = list()

def send_date(days):
    date = datetime.date.today() + datetime.timedelta(days)
    veckodag = dagar[int(date.strftime('%w'))]
    datum = date.strftime('%d')
    manad = date.strftime('%m')
    return veckodag + ' ' + datum + '/' + manad

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'bot':
        for x in range(1, 3):

            msg_set.append(await message.channel.send(send_date(x))) # skickar meddelandet och lägger till det i listan msg_set
            print(msg_set)
            await msg_set[-1].add_reaction(emoji_yes) #lägger till reaktionerna ja och nej på den sist sända meddelandet
            await msg_set[-1].add_reaction(emoji_no)

@commands.Cog.listener()
async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
    channel = self.bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = self.bot.get_user(payload.user_id)
    if not user:
        user = await self.bot.fetch_user(payload.user_id)
    await message.remove_reaction(payload.emoji, user)

client.run(TOKEN)
