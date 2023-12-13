from datetime import timedelta

import discord
from discord import app_commands
from discord.ext import commands

invite_links = ["*.gg/*", "*discord.com/invite*", "*discord.gg*"]


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.guild_only()
    async def automod(self, ctx, log_channel: discord.TextChannel):
        actions = [
            discord.AutoModRuleAction(),
            discord.AutoModRuleAction(channel_id=log_channel.id),
            discord.AutoModRuleAction(duration=timedelta(hours=1)),
        ]

        await ctx.guild.create_automod_rule(
            name="Anti Invite",
            event_type=discord.AutoModRuleEventType.message_send,
            trigger=discord.AutoModTrigger(
                type=discord.AutoModRuleTriggerType.keyword, keyword_filter=invite_links
            ),
            enabled=True,
            actions=actions
        )
        await ctx.response.send_message("✅ Erfolgreich eingerichtet.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Base(bot))
