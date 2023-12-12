import discord
from discord.ext import commands
from discord.ui import UserSelect, RoleSelect, ChannelSelect
from discord import app_commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def select(self, ctx):
        await ctx.response.send_message(view=Dropdown())


async def setup(bot):
    await bot.add_cog(Base(bot))


class Dropdown(discord.ui.View):
    @discord.ui.select(cls=RoleSelect, placeholder="Wähle Rollen aus", min_values=1, max_values=3)
    async def role_callback(self, interaction, select):
        mentions = [f"{roles.mention}" for roles in select.values]
        role_list = ", ".join(mentions)
        await interaction.response.send_message(f"Du hast folgende Rollen ausgewählt: {role_list}")

    @discord.ui.select(cls=ChannelSelect, placeholder="Wähle einen Channel", min_values=1, max_values=1)
    async def channel_callback(self, interaction, select):
        await interaction.response.send_message(f"Du hast {select.values[0].mention} gewählt.")

    @discord.ui.select(cls=UserSelect, placeholder="Wähle einen User", min_values=1, max_values=1)
    async def user_callback(self, interaction, select):
        await interaction.response.send_message(f"Du hast {select.values[0].mention} gewählt.")
