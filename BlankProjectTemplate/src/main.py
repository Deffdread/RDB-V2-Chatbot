import discord
from imgurpython import ImgurClient
from discord.ext import commands
# from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import aiohttp
import random
import youtube_dl
# CLIENT_ID = "1fd3ef04daf8cab"
# CLIENT_SECRET = "f963e574e8e3c17993c933af4f0522e1dc01e230"
# GIPHY_API_KEY = "dc6zaTOxFJmzC"

BOT_PREFIX = ("?", "!")
client = commands.Bot(command_prefix='.')
players = {}


# def __init__(self, bot):
#     self.bot = bot
#     self.imgur = ImgurClient(CLIENT_ID, CLIENT_SECRET)


    # @commands.command(pass_context=True, no_pm=True)
    # async def gif(self, ctx, *keywords):
    #     """Retrieves first search result from giphy"""
    #     if keywords:
    #         keywords = "+".join(keywords)
    #     else:
    #         await self.bot.send_cmd_help(ctx)
    #         return

    #     url = ("http://api.giphy.com/v1/gifs/search?&api_key={}&q={}"
    #            "".format(GIPHY_API_KEY, keywords))

    #     async with aiohttp.get(url) as r:
    #         result = await r.json()
    #         if r.status == 200:
    #             if result["data"]:
    #                 await self.bot.say(result["data"][0]["url"])
    #             else:
    #                 await self.bot.say("No results found.")
    #         else:
    #             await self.bot.say("Error contacting the API")

# client = discord.Client()

@client.event
async def on_ready():
    print("Bot is running")

@client.event
async def on_message(message):
    if message.author == client.user: 
        return   #Ensures the bot does not respond to itself
    if message.content == "Whats your name?":
        await client.send_message(message.channel, "Red")

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

client.run("NTAxODYzNzk3NTYxMjI5MzIz.Dqfkqg.v2MkSoR25EQrTWgo5LynD0h3bXk")