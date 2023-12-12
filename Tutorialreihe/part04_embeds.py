import discord
from discord.ext import commands
from discord import app_commands


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f"{self.user} ist online")

    async def setup_hook(self):
        await self.tree.sync()


bot = Bot()


@bot.tree.command(name="uerinfo", description="Zeige Infos über einen User")
@app_commands.describe(alter="Das Alter", user="Gib einen User an")
async def info(
        ctx,
        alter: app_commands.Range[int, 1, 99],
        user: discord.Member = None,
):
    if user is None:
        user = ctx.user

    embed = discord.Embed(
        title=f"Infos über {user.name}",
        description=f"Hier siehst du alle Details über {user.mention}",
        color=discord.Color.blue()
    )

    time = discord.utils.format_dt(user.created_at, "R")

    embed.add_field(name="Account erstellt", value=time, inline=False)
    embed.add_field(name="ID", value=user.id)
    embed.add_field(name="Alter", value=alter)

    embed.set_thumbnail(url=ctx.user.display_avatar.url)
    embed.set_footer(text="Das ist ein Footer")

    await ctx.response.send_message(embed=embed)


bot.run("")  # hier bot token einfügen
