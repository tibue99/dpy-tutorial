import discord
from discord.ext import commands
from discord import app_commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def button(self, ctx):
        await ctx.response.send_message(view=TutorialView(), ephemeral=True)


async def setup(bot):
    await bot.add_cog(Base(bot))


class TutorialView(discord.ui.View):
    @discord.ui.button(label="Keks", style=discord.ButtonStyle.primary, emoji="🍪")
    async def button_callback(self, interaction, button):
        await interaction.response.edit_message(content="Keks1")
        await interaction.followup.send("Keks2", ephemeral=True)
