# In der Main-Datei kann der Status direkt beim Start gesetzt werden
#
# intents = discord.Intents.default()
# activity = discord.Activity(type=discord.ActivityType.watching, name="Coding Keks")
# status = discord.Status.dnd

# bot = commands.Bot(
#     command_prefix="!",
#     intents=intents,
#     activity=activity,
#     status=status
# )


import discord
from discord import app_commands
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.choices(typ=[
        app_commands.Choice(name="game", value="game"),
        app_commands.Choice(name="stream", value="stream")
    ])
    async def activity(
        self, interaction,
        typ: app_commands.Choice[str],
        name: str
    ):
        if typ.value == "game":
            act = discord.Game(name=name)
        else:
            act = discord.Streaming(
                name=name,
                url="https://www.twitch.tv/keks"
            )
        await self.bot.change_presence(activity=act, status=discord.Status.online)
        await interaction.response.send_message("Status wurde geändert!")


async def setup(bot):
    await bot.add_cog(Commands(bot))
