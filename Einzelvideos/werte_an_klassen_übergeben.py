import discord
from discord import app_commands
from discord.ext import commands


class Button(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def button1(self, ctx):
        await ctx.response.send_message("Klicke hier", view=TutorialView(ctx.user))


async def setup(bot):
    await bot.add_cog(Button(bot))


class TutorialView(discord.ui.View):
    def __init__(self, user):
        self.user = user
        super().__init__(timeout=None)

    @discord.ui.button(label="Keks", style=discord.ButtonStyle.primary, emoji="🍪", custom_id="keks")
    async def button_callback1(self, interaction, button):
        if self.user.id != interaction.user.id:
            await interaction.response.send_message(
                "Du darfst diesen Button nicht benutzen!", ephemeral=True
            )
            return

        await interaction.response.send_message(
            f"{interaction.client.user.name} mag Kekse", ephemeral=True
        )

    @discord.ui.button(
        label="Pizza", style=discord.ButtonStyle.primary, emoji="🍕", custom_id="pizza"
    )
    async def button_callback2(self, interaction, button):
        button.disabled = True
        await interaction.response.edit_message(view=self)
