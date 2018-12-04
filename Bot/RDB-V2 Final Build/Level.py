## @file Level.py
#  @author Jason Tsui
#  @brief Implements methods for leveling system in Discord chat bot. Only provides functionality.
#  @date 11/10/2018

import discord
import asyncio
from discord.ext import commands

## @brief Class for implementing leveling system methods
class Level:

    ## @brief Initializes level module
    def __init__(self, client):
        self.client = client
        
    ## @brief Creates a member expereince profile
    #  @param users JSON Dictionary of members
    #  @param member Member that is being updated
    async def update_data(self,users,member):
        if not member.id in users:
            users[member.id] = {}
            users[member.id]['Experience'] = 0
            users[member.id]['Level'] = 1

    ## @brief Adds experience to a member expereince profile
    #  @param users JSON Dictionary of members
    #  @param member Member that is being updated
    #  @param exp Number of experience awarded to member
    async def add_experience(self,users, member, exp):
        users[member.id]['Experience'] += exp

    ## @brief Congradulates member for reaching next level in experience profile
    #  @param users JSON Dictionary of members
    #  @param member Member that is being updated
    #  @param channel Where bot outputs message
    async def level_up(self, users, member, channel):
        experience = users[member.id]['Experience']
        lvl_start = users[member.id]['Level']
        lvl_end = int(experience**(1/4))

        if lvl_start < lvl_end:
            await self.client.send_message(channel, '{} has leveled up to level {}'.format(member.mention, lvl_end))
            users[member.id]['Level'] = lvl_end

#Discord module loading
def setup(client):
        client.add_cog(Level(client))