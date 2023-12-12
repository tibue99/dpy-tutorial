import discord
from discord import app_commands
from discord.ext import commands


class Button(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(TutorialView())

    @app_commands.command()
    async def button1(self, interaction):
        await interaction.response.send_message("Klicke hier", view=TutorialView())

    @app_commands.command()
    async def button2(self, interaction):
        button = TutorialButton("Kekse sind cool")
        view = discord.ui.View()
        view.add_item(button)

        await interaction.response.send_message("Klicke hier", view=view)

    @app_commands.command()
    async def url_button(self, interaction):
        button = discord.ui.Button(label="GitHub", url="https://github.com/tibue99")
        view = discord.ui.View()
        view.add_item(button)

        await interaction.response.send_message("Klicke hier", view=view)


async def setup(bot):
    await bot.add_cog(Button(bot))


class TutorialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Keks", style=discord.ButtonStyle.primary, emoji="🍪", custom_id="keks", row=2
    )
    async def button_callback1(self, interaction, button):
        await interaction.response.send_message("Keks", ephemeral=True)

    @discord.ui.button(
        label="Pizza", style=discord.ButtonStyle.primary, emoji="🍕", custom_id="pizza", row=1
    )
    async def button_callback2(self, interaction, button):
        button.disabled = True

        # Alle Buttons deaktivieren
        # for child in self.children:
        #     child.disabled = True

        await interaction.response.edit_message(view=self)


class TutorialButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.green)

    async def callback(self, interaction):
        await interaction.response.send_message("Hey!", ephemeral=True)
