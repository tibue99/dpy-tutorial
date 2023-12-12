import discord
from discord.ext import commands
from discord import app_commands

foods = ["Pizza", "Pommes", "Döner"]


async def get_food(interaction: discord.Interaction, current: str):
    choices = [
        app_commands.Choice(name=food, value=food)
        for food in foods if current.lower() in food.lower()
    ]

    if "99" in interaction.user.display_name:
        return choices + [app_commands.Choice(name="Kekse", value="Kekse")]

    return choices


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.autocomplete(auswahl=get_food)
    async def essen(self, ctx, auswahl: str):
        await ctx.response.send_message(f"Du hast ✨ **{auswahl}** ✨ gewählt")


async def setup(bot):
    await bot.add_cog(Base(bot))
