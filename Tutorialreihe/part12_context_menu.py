import discord
from discord.app_commands import ContextMenu
from discord.ext import commands


class Context(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.bot.tree.add_command(ContextMenu(name="Zeige die ID", callback=self.get_id))
        self.bot.tree.add_command(ContextMenu(name="Stups", callback=self.stups))

    async def get_id(self, ctx, message: discord.Message):
        await ctx.response.send_message(f"Hier ist die Message ID: {message.id}")

    async def stups(self, ctx, member: discord.Member):
        await ctx.response.send_message(f"{ctx.user.mention} hat {member.mention} angestupst!")


async def setup(bot):
    await bot.add_cog(Context(bot))
