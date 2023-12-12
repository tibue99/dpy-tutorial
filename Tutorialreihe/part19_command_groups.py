import discord
from discord import app_commands
from discord.ext import commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    eat = app_commands.Group(name="eat", description="Essen ist lecker")

    @eat.command()
    async def cookie(self, ctx):
        await ctx.response.send_message("Du hast dir einen Keks gegönnt 🍪")

    @eat.command()
    async def pizza(self, ctx):
        await ctx.response.send_message("Du hast dir eine Pizza gegönnt 🍕")

    give = app_commands.Group(
        name="give",
        default_permissions=discord.Permissions(administrator=True),
        description="Gib jemandem etwas",
    )

    keks = app_commands.Group(parent=give, name="keks", description="Verteile Kekse")

    @keks.command()
    async def schoko(self, ctx):
        await ctx.response.send_message("Ein legendärer Schokokeks wurde vergeben")

    @keks.command()
    async def subway(self, ctx):
        await ctx.response.send_message("Subway Cookie wurde vergeben!!!")


async def setup(bot):
    await bot.add_cog(Base(bot))
