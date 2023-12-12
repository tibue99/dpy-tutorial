# Für dieses Beispiel muss der Server Member Intent im Dev Portal und in der Main-Datei aktiviert sein
#
# intents = discord.Intents.default()
# intents.members = True
#
# bot = commands.Bot(
#     command_prefix="!",
#     intents=intents,
#     debug_guilds=[123456789],  # hier server id einfügen
# )

import discord
from discord import app_commands
from discord.ext import commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def greet(self, interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title="Willkommen",
            description=f"Hey {member.mention}",
            color=discord.Color.orange()
        )

        channel = await self.bot.fetch_channel(123456789)  # hier channel id einfügen
        await channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Base(bot))
