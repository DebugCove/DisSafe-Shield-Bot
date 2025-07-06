import discord
from discord.ext import commands
from discord import app_commands, Interaction


class Geral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ping', description='Testa se o bot está online.')
    async def ping(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title='Pong!',
            description=f'Latência: {round(self.bot.latency * 1000)}ms',
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(Geral(bot))
