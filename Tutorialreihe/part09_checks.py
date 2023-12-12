import discord
from discord import app_commands
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.tree.on_error = self.on_app_command_error

    @app_commands.command(description="Kicke einen Member")
    @app_commands.default_permissions(administrator=True, kick_members=True)
    @app_commands.guild_only()
    @app_commands.describe(member="Wähle einen Member")
    async def kick(self, interaction, member: discord.Member):
        try:
            await member.kick()
        except discord.Forbidden:
            await interaction.response.send_message(
                "Ich habe keine Berechtigung, um diesen Member zu kicken", ephemeral=True
            )
            return
        await interaction.response.send_message(f"{member.mention} wurde gekickt!")

    @app_commands.command()
    @app_commands.checks.has_permissions(administrator=True)
    async def hallo(self, interaction):
        await interaction.response.send_message("Hey")

    @commands.Cog.listener()
    async def on_app_command_error(self, ctx, error):
        if isinstance(error, app_commands.CheckFailure):
            await ctx.response.send_message(f"Nur Admins dürfen diesen Befehl ausführen!", ephemeral=True)
            return

        await ctx.response.send_message(f"Es ist ein Fehler aufgetreten: ```{error}```", ephemeral=True)
        raise error


async def setup(bot):
    await bot.add_cog(Admin(bot))
