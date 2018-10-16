import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is running")

@client.event
async def on_message(message):
    if message.author == client.user: 
        return   #Ensures the bot does not respond to itself
    if message.content == "Whats your name?":
        await client.send_message(message.channel, "Red")

client.run("NTAxMjU5ODY5OTQ5Nzg4MTYy.DqWz0g.exYDC0UtqHUsTBXYO8HpNo1C_zk")