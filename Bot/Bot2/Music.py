import discord
import asyncio
import youtube_dl
from discord.ext import commands

## @brief Class for implementing a music player
class Music:
    players = {}
    queues = {}

    ## @brief Initializes music module
    def __init__(self, client):
        self.client = client
        

    ## @brief Bot joins channel
    #  @details Called by !join
    @commands.command(pass_context = True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await self.client.join_voice_channel(channel)

    ## @brief Bot leaves channel
    #  @details Called by !leave
    @commands.command(pass_context = True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server) #Voice client associated with server
        await voice_client.disconnect()

    ## @brief Bot plays music
    #  @details Must have bot join channel first before playing. Called by !play [url]
    #  @param url youtube url
    @commands.command(pass_context = True)
    async def play(self, ctx, url):
        #Bot2.ONEDIT = 1
        try:
            server = ctx.message.server
            voice_client = self.client.voice_client_in(server) #Instance of the bot in the voice channel
            player = await voice_client.create_ytdl_player(url, after=lambda: self.queue_play(server.id)) #Creates yt stream to voice client
            self.players[server.id] = player
            player.start() #Starts player
        except:
            await self.client.say("Bot not in channel, use !join first")


    ## @brief Bot pauses music
    #  @details Must have bot playing music
    @commands.command(pass_context=True)
    async def pause(self, ctx):
        playerid = ctx.message.server.id
        self.players[playerid].pause()    

    ## @brief Bot stop music
    #  @details Must have bot playing music
    @commands.command(pass_context=True)
    async def stop(self, ctx):
        playerid = ctx.message.server.id
        self.players[playerid].stop()

    ## @brief Bot resume music
    #  @details Must have bot on pause
    @commands.command(pass_context=True)
    async def resume(self, ctx):
        playerid = ctx.message.server.id
        self.players[playerid].resume()   

    ## @brief Bot queues music
    #  @details Must have bot on pause
    #  @param url youtube url
    @commands.command(pass_context=True)
    async def queue(self, ctx,url):
        server = ctx.message.server 
        voice_client = self.client.voice_client_in(server) #Instance of voice in server
        player = await voice_client.create_ytdl_player(url, after=lambda: self.queue_play(server.id)) #Creates yt stream to voice client
        if server.id in self.queues: #If something already in queue
            self.queues[server.id].append(player)
        else: #Empty queue
            self.queues[server.id] = [player]
        await self.client.say('Queued successful')

    ## @brief Helper function to run next music player on queue
    def queue_play(self, serverid):
        if self.queues[serverid] != []:
            player = self.queues[serverid].pop(0)
            self.players[id] = player
            player.start()
    
def setup(client):
        client.add_cog(Music(client))