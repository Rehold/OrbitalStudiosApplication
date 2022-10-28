# Imports
import aiohttp
import discord
from discord.ext import commands
from discord import app_commands, Colour
import platform
import psutil
import json


# Cog subclass
class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = (
            bot  # Allows us to use the bot outside of the __init__ function
        )
        self.bot.tree.add_command(
            meme
        )  # Register the slash command in our bot


configjson = open("config.json")
# config should be file name, () gotta be var above
config = json.load(configjson)
serverID = int(config['bot']["serverID"])
mainColor = config['brandingColors']["mainColor"]
errorColor = config['brandingColors']["errorColor"]
successColor = config['brandingColors']["successColor"]
configjson.close()


# note!! need to change to cmd groups
@app_commands.command(
    name="meme", description="Gives you a random meme from the internet."
)
@app_commands.guilds(serverID)
async def meme(interaction: discord.Interaction):
    session = aiohttp.ClientSession()

    response = await session.get("https://meme-api.herokuapp.com/gimme")
    response = await response.json()
    await response.close()

    if response["nsfw"] == True:
        embed = discord.Embed(
            title="🔞 NSFW Meme",
            description="This meme is marked as NSFW, so I can't send it here.",
            colour=Colour.from_str(errorColor),
        )
        await interaction.response.send_message(embed=embed)

    embed = discord.Embed(
        title="🤣 Random Meme",
        description=f"Here is a random meme for you!",
        colour=Colour.from_str(mainColor),
    )
    embed.set_image(url=response["url"])
    embed.set_footer(text=f"👍 {response['ups']} | 💬 {response['postLink']}")
    await interaction.response.send_message(embed=embed)

# Sets up the cog
async def setup(bot):
    await bot.add_cog(Meme(bot))
