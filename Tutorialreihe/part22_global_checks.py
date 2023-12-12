from discord import app_commands
from discord.ext import commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.tree.on_error = self.on_app_command_error
        bot.tree.interaction_check = self.bot_check

    async def bot_check(self, interaction):
        if interaction.user.id != 123456789:  # hier user ID einfügen
            await interaction.response.send_message(
                "Du bist nicht würdig genug, um diesen Befehl zu nutzen!")
            return False
        return True

    async def interaction_check(self, interaction):  # Cog check
        if interaction.user.voice is None:
            await interaction.response.send_message("Tritt erst einem Voice Channel bei.")
            return False
        return True

    @app_commands.command()
    async def hey(self, ctx):
        await ctx.response.send_message("Hey")

    @commands.Cog.listener()
    async def on_app_command_error(self, interaction, error):
        if isinstance(error, app_commands.CheckFailure):
            return
        raise error


async def setup(bot):
    await bot.add_cog(Base(bot))
