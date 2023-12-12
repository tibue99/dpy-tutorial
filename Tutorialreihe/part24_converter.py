import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import ColorConverter


class ColorTransformer(app_commands.Transformer):
    async def transform(self, interaction: discord.Interaction, value: str) -> discord.Color:
        return await ColorConverter().convert(interaction, value)


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def converter(self, ctx, color: app_commands.Transform[discord.Color, ColorTransformer]):
        embed = discord.Embed(
            title="Titel",
            color=color
        )
        await ctx.response.send_message(embed=embed, ephemeral=True)

    @converter.error
    async def color_error(self, ctx, error):
        if isinstance(error, app_commands.TransformerError):
            await ctx.response.send_message("Du hast eine ungültige Farbe gewählt", ephemeral=True)
            return
        raise error

    async def on_app_command_error(self, interaction, error):
        if isinstance(error, app_commands.TransformerError):
            return
        raise error


async def setup(bot):
    await bot.add_cog(Base(bot))
