import discord
from discord import app_commands
from discord.ext import commands


class ModalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def modal(self, ctx):
        modal = TutorialModal()
        await ctx.response.send_modal(modal)

    @app_commands.command()
    async def button_modal(self, ctx):
        await ctx.response.send_message("Hey", view=TutorialView())


async def setup(bot):
    await bot.add_cog(ModalCog(bot))


class TutorialModal(discord.ui.Modal, title="Erstelle ein Embed"):
    embed_title = discord.ui.TextInput(
        label="Embed Titel",
        placeholder="Placeholder"
    )
    embed_description = discord.ui.TextInput(
        label="Embed Beschreibung",
        placeholder="Placeholder",
        style=discord.TextStyle.long
    )

    async def on_submit(self, interaction):
        embed = discord.Embed(
            title=self.embed_title.value,
            description=self.embed_description.value,
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)


class TutorialView(discord.ui.View):
    @discord.ui.button(label="Klicke hier")
    async def button_callback(self, interaction, button):
        await interaction.response.send_modal(TutorialModal())
