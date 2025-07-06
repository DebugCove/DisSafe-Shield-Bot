from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot ligado  como {self.bot.user}')
        try:
            synced = await self.bot.tree.sync()
            print(f'{len(synced)} comandos carregados com sucesso')
        except Exception as error:
            print(f'Erro ao tentar sicronizar os comandos: {error}')


async def setup(bot):
    await bot.add_cog(Events(bot))
