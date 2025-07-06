from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot connected as {self.bot.user}')
        try:
            synced = await self.bot.tree.sync()
            print(f'{len(synced)} commands loaded successfully')
        except Exception as error:
            print(f'Error when trying to synchronise commands: {error}')


async def setup(bot):
    await bot.add_cog(Events(bot))
