import discord
from discord.ext import commands
from discord import app_commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.tree.on_error = self.on_app_command_error

    @app_commands.command(description="Kickt einen Member")
    @app_commands.describe(member="Wähle einen Member")
    async def kick(self, ctx, member: discord.Member):
        try:
            await member.kick()
        except discord.Forbidden:
            await ctx.response.send_message(
                "Ich habe keine Berechtigung, um diesen Member zu kicken"
            )
            return
        await ctx.response.send_message(f"{member.mention} wurde gekickt!")

    async def on_app_command_error(self, ctx, error):
        await ctx.response.send_message(f"Es ist ein Fehler aufgetreten: ```{error}```")


async def setup(bot):
    await bot.add_cog(Admin(bot))
