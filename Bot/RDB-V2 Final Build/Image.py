## @file Image.py
#  @author Abdul Elrahwan
#  @brief Implements methods for Imgur image search in Discord chat bot.
#  @date 11/14/2018

import discord
import asyncio
import aiohttp
import functools
from imgurpython import ImgurClient
from discord.ext import commands

## @brief Class for implementing image search methods
class Image:

    ## @brief Initializes image module
    def __init__(self, client):
        self.client = client
        self.imgur = ImgurClient("65e2a071cb50a49", "c338792bfe4b3ec23b3a874dc1f934c3f1fc7adc")

    ## @brief Helper function for image search
    #  @param ctx Discord context
    @commands.group(name="imgur", no_pm=True, pass_context=True)
    async def imgurService(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.client.send_cmd_help(ctx)

    ## @brief Image search function
    #  @param ctx Discord chat context
    #  @param tag String attribute to be searched for
    @imgurService.command(pass_context=True, name="search")
    async def imgur_search(self, ctx, *, tag: str):
        params = functools.partial(self.imgur.gallery_search, tag,
                                 advanced=None, sort='time',
                                 window='all', page=0)

        
        params = self.client.loop.run_in_executor(None, params)

        #Retreive top result of tag and display
        try:
            results = await asyncio.wait_for(params, timeout=50)
        except asyncio.TimeoutError:
            
            await self.client.say("Took too long")
        else:
            
            if results:
                msg = "Top result"
                for r in results[:1]:
                    msg += r.gifv if hasattr(r, "gifv") else r.link
                    msg += "\n"
                await self.client.say(msg)
            else:
                await self.client.say("No results")

           
#Discord module loading
def setup(client):
        client.add_cog(Image(client))
