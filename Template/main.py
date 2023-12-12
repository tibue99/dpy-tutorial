import asyncio

import discord
import ezcord


class TutorialBot(ezcord.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())

    async def setup_hook(self):
        await super().setup_hook()
        await self.tree.sync()

    async def on_ready(self):
        print(f"{self.user} ist online")


async def main():
    async with TutorialBot() as bot:
        bot.load_cogs("cogs")  # Load all cogs in the "cogs" folder
        await bot.start("TOKEN")


if __name__ == "__main__":
    asyncio.run(main())
