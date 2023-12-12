from discord import app_commands
from discord.ext import commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def reaction(self, interaction):
        await interaction.response.send_message("Hey")
        message = await interaction.original_response()
        await message.add_reaction("🍪")

    @app_commands.command()
    async def edit(self, interaction):
        await interaction.response.send_message("Hey", ephemeral=True)
        await interaction.edit_original_response(content="🍪")


async def setup(bot):
    await bot.add_cog(Base(bot))
