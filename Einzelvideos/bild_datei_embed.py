import discord
from discord.ext import commands
from discord import app_commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def bild(self, ctx):
        embed = discord.Embed(
            title="Lecker",
            color=discord.Color.blue()
        )
        file = discord.File(f"cookie.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await ctx.response.send_message(embed=embed, file=file)


async def setup(bot):
    await bot.add_cog(Base(bot))
