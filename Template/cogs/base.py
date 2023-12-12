import discord
from discord.ext import commands
from discord import app_commands


class Base(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description="hello")
    async def hello(self, ctx: discord.Interaction):
        await ctx.response.send_message(f"Hey {ctx.user.mention}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Base(bot))
