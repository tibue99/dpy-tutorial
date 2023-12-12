from discord import app_commands
from discord.ext import commands


async def custom_check(ctx):
    return ctx.user.id == 123456789  # hier user ID einfügen


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.tree.on_error = self.on_app_command_error

    @app_commands.command()
    @app_commands.check(custom_check)
    async def hallo(self, ctx):
        await ctx.response.send_message("Hey")

    @commands.Cog.listener()
    async def on_app_command_error(self, ctx, error):
        if isinstance(error, app_commands.CheckFailure):
            await ctx.response.send_message(f"Du bist nicht würdig genug, um diesem Befehl zu nutzen!", ephemeral=True)
            return

        await ctx.response.send_message(f"Es ist ein Fehler aufgetreten: ```{error}```", ephemeral=True)
        raise error


async def setup(bot):
    await bot.add_cog(Base(bot))
