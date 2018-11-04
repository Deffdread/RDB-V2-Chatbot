import discord
from threading import Semaphore
from discord.ext import commands

#Bot specific code
TOKEN = 'NTA1ODQ5NDMwODA5NzcyMDMy.DrZmJg.sPGSaZgOM8GgSZvJYQ2MgiThutU'

client = commands.Bot(command_prefix = '!') #Stuff before entering command

#Global variables
ONDELETE = 0 #Variable for blocking on_message_delete when command !clear is called. 

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
    await client.process_commands(message)

#Notifies community server when message is deleted
@client.event
async def on_message_delete(message):
    global ONDELETE
    if ONDELETE > 0:
        ONDELETE -= 1
        return None
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

#Saids owner of server
#!owner
@client.command()
async def owner():
    await client.say('Jason Tsui')

#Echos message in channel
#!echo
@client.command()
async def echo(*args):
    output = " "
    for word in args:
        output = output + word
        output += " "
    await client.say(output)

#Clears amount messages in channel. Default is 5 messages unless specified. +1 is for deleting !clear command
#!clear([number of messages])
@client.command(pass_context=True)
async def clear(ctx,amount=5):
    global ONDELETE
    ONDELETE = amount+1
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)+1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('{} Messages cleared by admin'.format(amount))

client.run(TOKEN)






