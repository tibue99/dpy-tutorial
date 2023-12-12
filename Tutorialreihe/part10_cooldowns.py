from discord import app_commands
from discord.ext import commands
from discord.app_commands import checks


class Cooldown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.tree.on_error = self.on_app_command_error

    @app_commands.command()
    @checks.cooldown(1, 10, key=lambda i: (i.guild_id, i.user.id))
    async def hey(self, interaction):
        await interaction.response.send_message("Hey")

    @commands.Cog.listener()
    async def on_app_command_error(self, ctx, error):
        if isinstance(error, app_commands.CommandOnCooldown):
            await ctx.response.send_message(f"Du musst noch warten.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Cooldown(bot))
