import discord
from discord.ext import commands
from discord import app_commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def embed(self, ctx, hexcode: str):
        hex_string = f"0x{hexcode}"
        color = int(hex_string, 16)

        embed = discord.Embed(
            description="Dies ist ein sehr cooler Text"
                        "\n\n🔹 Kekse sind lecker",
            color=color
        )
        embed.set_thumbnail(url=ctx.user.display_avatar)
        await ctx.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Base(bot))
