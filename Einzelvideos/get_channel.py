import discord
from discord.ext import commands
from discord import app_commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel_id = 123456789  # Hier Channel ID einfügen

        # Variante 1
        channel = self.bot.get_channel(channel_id)

        # Variante 2
        try:
            channel = await self.bot.fetch_channel(channel_id)
        except discord.Forbidden:
            print("Keine Rechte")
            return

        if channel is not None:
            await channel.send("Kekse sind lecker!")
        else:
            print("Channel wurde nicht gefunden :(")

    @app_commands.command()
    async def say(self, ctx):
        channel_id = 123456789  # Hier Channel ID einfügen

        # Variante 3 (Geht auch mit fetch)
        channel = ctx.guild.get_channel(channel_id)

        # Variante 4 (Geht auch mit dem Namen des Channels)
        channel = discord.utils.get(ctx.guild.text_channels, id=channel_id)

        if channel is not None:
            await channel.send("Kekse sind schmackhaft!")
            await ctx.response.send_message("Nachricht gesendet.")
        else:
            await ctx.response.send_message("Channel wurde nicht gefunden :(")


async def setup(bot):
    await bot.add_cog(Base(bot))
