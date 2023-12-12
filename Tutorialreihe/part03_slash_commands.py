import discord
from discord import app_commands
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f"{self.user} ist online")

    async def setup_hook(self):
        await self.tree.sync()


bot = Bot()


@bot.tree.command(description="Grüße einen User")
@app_commands.describe(user="Grüße einen User")
async def greet(ctx, user: discord.User):
    await ctx.response.send_message(f"Hallo {user.mention}")


@bot.tree.command(description="Lass den Bot eine Nachricht senden")
@app_commands.describe(
    text="Der Text, den du senden möchtest",
    channel="Der Channel, in den du die Nachricht senden möchtest"
)
async def say(ctx, text: str, channel: discord.TextChannel):
    await channel.send(text)
    await ctx.response.send_message("Nachricht gesendet", ephemeral=True)


bot.run("")  # hier bot token einfügen
