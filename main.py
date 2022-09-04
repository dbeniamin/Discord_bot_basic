import discord

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):

        if str(message.author) == "SirSnake#0257":  # user name with hash code
            await message.channel.send("Hello " + str(message.author) + "!")
        else:
            await message.channel.send("Hello, I am a test bot.")


client.run("Discord Token")  # copy your token from the developer portal

#To hide the token, you can do it a .env file.
# VARIABLE_NAME=your_token_here