import discord
from discord.ext import commands
from discord import app_commands


class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="Starte das Radio")
    async def play(self, ctx):
        if ctx.user.voice is None:
            return await ctx.response.send_message("Du musst erst einem Voice Channel beitreten.")

        if not ctx.user.voice.channel.permissions_for(ctx.guild.me).connect:
            return await ctx.response.send_message("Ich habe keine Rechte, um deinem Channel beizutreten.")

        if ctx.guild.voice_client is None:
            await ctx.user.voice.channel.connect()  # Bot ist in keinem Voice Channel
        else:
            await ctx.guild.voice_client.move_to(ctx.user.voice.channel)  # Bot ist schon in einem anderen Voice Channel

        if ctx.guild.voice_client.is_playing():
            ctx.guild.voice_client.stop()

        ctx.guild.voice_client.play(
            discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio1.mp3")
        )
        await ctx.response.send_message("Das Radio wurde gestartet")

    @app_commands.command(description="Stoppe das Radio")
    async def leave(self, ctx):
        if ctx.guild.voice_client is None:
            return await ctx.response.send_message("Ich bin mit keinem Voice Channel verbunden.")

        await ctx.guild.voice_client.disconnect()
        await ctx.response.send_message("Bis bald")


async def setup(bot):
    await bot.add_cog(Radio(bot))
