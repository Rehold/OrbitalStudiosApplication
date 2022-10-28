# Imports
import discord
from discord.ext import commands
from discord import app_commands, Colour
import platform
import psutil
import json


# Cog subclass
class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = (
            bot  # Allows us to use the bot outside of the __init__ function
        )
        self.bot.tree.add_command(
            serverinfo
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
    name="serverinfo", description="Get infomation about the server."
)
@app_commands.guilds(serverID)
async def serverinfo(interaction: discord.Interaction):
    embed = discord.Embed(title="📊 Server Info", colour=Colour.from_str(mainColor))
    embed.add_field(name="• General:", value=f"> Name: ``{interaction.guild.name}``\n> ID: ``{interaction.guild.id}``\n> Owner: {interaction.guild.owner.mention}\n> Created at: <t:{interaction.guild.created_at.timestamp():.0f}:F>")
    embed.add_field(name="• Members:", value=f"> Total: ``{interaction.guild.member_count}``\n> Humans: ``{len([m for m in interaction.guild.members if not m.bot])}``\n> Bots: ``{len([m for m in interaction.guild.members if m.bot])}``")
    embed.add_field(name="• Channels:", value=f"> Total: ``{len(interaction.guild.channels)}``\n> Text: ``{len(interaction.guild.text_channels)}``\n> Voice: ``{len(interaction.guild.voice_channels)}``")
    embed.add_field(name="• Roles:", value=f"> Total: ``{len(interaction.guild.roles)}``\n> Highest: ``{interaction.guild.roles[-1]}``")
    await interaction.response.send_message(embed=embed)

# Sets up the cog
async def setup(bot):
    await bot.add_cog(Serverinfo(bot))
