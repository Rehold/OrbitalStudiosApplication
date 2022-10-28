# Imports
from time import perf_counter

import discord
from discord.ext import commands
from discord import app_commands, Colour
import platform
import psutil
import json


# Cog subclass
class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = (
            bot  # Allows us to use the bot outside of the __init__ function
        )
        self.bot.tree.add_command(
            ping
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
    name="ping", description="Get the latency of the bot."
)
@app_commands.guilds(serverID)
async def ping(interaction: discord.Interaction):
    # code
    start = perf_counter()
    await interaction.client.database.db.command("ping")
    end = perf_counter()
    dblatency = end - start
    embed = discord.Embed(title=":ping_pong: Pong!", colour=Colour.from_str(mainColor))
    embed.add_field(
        name="• Bot latency:",
        value=f"> ``{round(interaction.client.latency * 1000)}ms``",
    )
    embed.add_field(
        name="• Database latency:", value=f"> ``{round(dblatency * 1000)}ms``"
    )
    await interaction.response.send_message(embed=embed)




# Sets up the cog
async def setup(bot):
    await bot.add_cog(Ping(bot))
