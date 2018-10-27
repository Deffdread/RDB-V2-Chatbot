import discord
from discord.ext import commands

#Bot specific code
TOKEN = 'NTA1ODQ5NDMwODA5NzcyMDMy.DrZmJg.sPGSaZgOM8GgSZvJYQ2MgiThutU'

client = commands.Bot(command_prefix = '.') #Stuff before entering command


#Detects when bot is ready
#Run command when bot is executing
@client.event
async def on_ready():
    print('Bot is ready')

#Repeats message to terminal
@client.event
async def on_message(message):
    author = message.author #who typed the message
    content = message.content #string message typed
    print('{}:{}'.format(author, content)) #prints as author: message into terminal

    if message.content == "botclose":
        client.close()


#Notifies community server when message is deleted
@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content 
    channel = message.channel
    await client.send_message(channel, 'Message deleted by {}'.format(author))#Message channel and message itself

#Notifies community server when message is edited
@client.event
async def on_message_edit(before,after):
    author = before.author
    content = before.content 
    channel = before.channel
    await client.send_message(channel, 'Message edited by {}'.format(author))#Message channel and message itself


client.run(TOKEN)






