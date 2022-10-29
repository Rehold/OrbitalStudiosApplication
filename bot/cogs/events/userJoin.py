# Imports
from time import perf_counter
import discord
from discord.ext import commands
import json


# Cog subclass
class EventsMemberAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = (
            bot  # Allows us to use the bot outside of the __init__ function
        )

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        dict = {
            "joinDate": member.joined_at,
            "userName": member.name,
        }
        await self.bot.database.users.update_one({"_id": member.id}, {"$set": dict}, upsert=True)


# Sets up the cog
async def setup(bot):
    await bot.add_cog(EventsMemberAdd(bot))