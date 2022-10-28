# Imports
import discord
from discord.ext import commands
from discord import app_commands, Colour
import platform
import psutil
import json


# Cog subclass
class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = (
            bot  # Allows us to use the bot outside of the __init__ function
        )
        self.bot.tree.add_command(
            userinfo
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
    name="userinfo", description="View information about an user."
)
@app_commands.guilds(serverID)
@app_commands.describe(user="The user to view information about.")
async def userinfo(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        user = interaction.user

    embed = discord.Embed(title="👤 User info", colour=Colour.from_str(mainColor))
    embed.add_field(name="• User details:", value=f"> ID: ``{user.id}``\n> Joined at: <t:{user.joined_at.timestamp():.0f}:F>\n> Account created: <t:{user.created_at.timestamp():.0f}:F>")
    embed.set_thumbnail(url=user.display_avatar.url)
    await interaction.response.send_message(embed=embed)




# Sets up the cog
async def setup(bot):
    await bot.add_cog(Userinfo(bot))
