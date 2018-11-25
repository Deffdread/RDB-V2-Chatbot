import discord
import asyncio
from discord.ext import commands

## @brief Class for miscellaneous methods
class Misc:

    ## @brief Initializes miscellaneous module
    def __init__(self, client):
        self.client = client
        

    ## @brief Bot prints the owner of the bot created
    #  @details Prints 'SE3XA3'. Called by !owner
    @commands.command()
    async def owner(self):
        await self.client.say('SE3XA3')

    #Echos message in channel
    #!echo
    @commands.command()
    async def echo(self,*args):
        output = " "
        for word in args:
            output = output + word
            output += " "
        await self.client.say(output)

    
def setup(client):
        client.add_cog(Misc(client))