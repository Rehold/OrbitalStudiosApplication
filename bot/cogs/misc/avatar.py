# Imports
import discord
from discord.ext import commands
from discord import app_commands, Colour
import platform
import psutil
import json


# Cog subclass
class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = (
            bot  # Allows us to use the bot outside of the __init__ function
        )
        self.bot.tree.add_command(
            avatar
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
    name="avatar", description="Get a avatar of an user."
)
@app_commands.guilds(serverID)
@app_commands.describe(user="The user to get the avatar of.")
async def avatar(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        user = interaction.user
    await interaction.response.send_message(content=f"{user.mention}'s avatar:\n\n{user.display_avatar.url}")


# Sets up the cog
async def setup(bot):
    await bot.add_cog(Avatar(bot))
