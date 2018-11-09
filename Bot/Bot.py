## @file Bot
#  @author Jason Tsui
#  @brief Provides the methods for corresponding discord bot
#  @date 9/11/2018

import discord
from threading import Semaphore
from discord.ext import commands
import asyncio

#Bot specific code
TOKEN = 'NTA1ODQ5NDMwODA5NzcyMDMy.DrZmJg.sPGSaZgOM8GgSZvJYQ2MgiThutU'

client = commands.Bot(command_prefix = '!') #Stuff before entering command

#Global variables
ONDELETE = 0 #Variable for blocking on_message_delete when command !clear is called. 
ONEDIT= 0 #Variable for blocking on_message_edit when command !displayembed is called.

## @brief Detects when bot is ready and outputs into terminal
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Bot is operational'))
    print('Bot is ready')

## @brief Displays messages sent in Discord server into terminal
#  @param message Message typed into Discord server
@client.event
async def on_message(message):
    author = message.author #who typed the message
    content = message.content #string message typed
    print('{}:{}'.format(author, content)) #prints as author: message into terminal
    await client.process_commands(message)


## @brief Bot notifies community server when message is deleted
#  @details Prints 'Message  deleted by <user>' into server
#  @param message Message that was typed into Discord server
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

## @brief Bot notifies community server when message is edited
#  @details Prints 'Message edited by <user>' into server
#  @param message Message that was typed into Discord server
@client.event
async def on_message_edit(before,after):
    global ONDEDIT
    if ONDEDIT > 0:
        ONDEDIT -= 1
        return None
    author = before.author
    content = before.content 
    channel = before.channel
    await client.send_message(channel, 'Message edited by {}'.format(author))#Message channel and message itself


## @brief Bot prints the owner of the bot created
#  @details Prints 'SE3XA3'. Called by !owner
@client.command()
async def owner():
    await client.say('SE3XA3')

#Echos message in channel
#!echo
@client.command()
async def echo(*args):
    output = " "
    for word in args:
        output = output + word
        output += " "
    await client.say(output)

## @brief Clears messages in channel
#  @details Clears <amount> messages in channel. Default is 5 messages after command unless specified. Called by !clears [int]
#  @param ctx Previous past message sent into server
#  @param amount Number of message to delete. Default is 5.
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

## @brief Assigns role to new member joining server
#  @param member Member that is joining the server
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = 'RoleTest') #Iterate through possible roles
    await client.add_roles(member,role) #Assigns role to member

## @brief Displays a particular news article fomr news.com.au about blackholes
#  @details !blackhole
@client.command()
async def blackhole():
    global ONDEDIT
    ONDEDIT = 1
    
    embed = discord.Embed(
        title = 'Astronomers piece together first image of black hole',
        description = 'ASTRONOMERS believe they’ve captured first images of the gravity and light-sucking monster that weighs as much as four million suns',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text ='An artists’ impression of a black hole. Astronomers are in the process of piecing together the first pictures captured of a black hole.Source:AFP')
    embed.set_image(url ='https://cdn.newsapi.com.au/image/v1/9fdbf585d17c95f7a31ccacdb6466af9')
    embed.set_thumbnail(url = 'https://pbs.twimg.com/profile_images/1026003052434677760/13MnHpm5_400x400.jpg')
    embed.set_author(name = 'www.news.com.au', icon_url ='https://www.newscorpaustralia.com/wp-content/uploads/2018/02/fullcolour_logo_onwhite_rgb-3.jpg')
    embed.add_field(name = 'Article', value = 'https://www.news.com.au/technology/science/space/astronomers-piece-together-first-image-of-black-hole/news-story/db09d5e8b215adbce46b96f74e8e0595', inline=False)
    #embed.add_field(name = 'Field', value = 'Field value', inline=True)
    #embed.add_field(name = 'Field', value = 'Field value', inline=True)

    await client.say(embed=embed)

client.run(TOKEN)






