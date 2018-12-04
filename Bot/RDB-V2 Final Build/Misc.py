## @file Misc.py
#  @author Jason Tsui
#  @brief Miscellaneous functions for bot. Does not have real application to chatbot. 
#  @date 11/01/2018


import discord
import asyncio
from discord.ext import commands

## @brief Class for miscellaneous methods
class Misc:

    ## @brief Initializes miscellaneous module
    def __init__(self, client):
        self.client = client
        

    ## @brief Bot prints the owner of the bot created
    #  @details Prints 'SE3XA3'
    @commands.command()
    async def owner(self):
        await self.client.say('SE3XA3')

    ## @brief Echo message in channel
    #  @param args String message to be echoed
    @commands.command()
    async def echo(self,*args):
        output = " "
        for word in args:
            output = output + word
            output += " "
        await self.client.say(output)

#Discord module loading
def setup(client):
        client.add_cog(Misc(client))