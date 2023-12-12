import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(user="Wähle einen User", auswahl="Beschreibung")
    @app_commands.choices(
        auswahl=[Choice(name="Ja", value="Ja"), Choice(name="Nein", value="Nein")]
    )
    async def hello(self, ctx, user: discord.User, auswahl: str = "Ja"):
        await ctx.respond(f"{auswahl}, {user.mention}")


async def setup(bot):
    await bot.add_cog(Base(bot))
