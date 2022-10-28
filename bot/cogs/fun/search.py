# Imports
import discord
from discord.ext import commands
from discord import app_commands, Colour
import platform
import psutil
import json


# Cog subclass
class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = (
            bot  # Allows us to use the bot outside of the __init__ function
        )
        self.bot.tree.add_command(
            search
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
    name="search", description="Search for something on the web."
)
@app_commands.guilds(serverID)
async def search(interaction: discord.Interaction, query: str):
    result = (
        "https://www.google.com/search?q="
        + query.replace(" ", "+")
        + "&safe=active&ssui=on"
    )
    embed = discord.Embed(
        title="🔍 Google Search",
        description=f"Searching google for ``{query}``...",
        colour=Colour.from_str(mainColor),
    )
    embed.add_field(name="• Results:", value=f"[Click here for results..]({result})")
    await interaction.response.send_message(embed=embed)


# Sets up the cog
async def setup(bot):
    await bot.add_cog(Search(bot))
