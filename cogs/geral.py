import discord
from discord.ext import commands
from discord import app_commands


class Geral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ping', description='Test if the bot is online.')
    async def ping(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title='Pong!',
            description=f'Latency: {round(self.bot.latency * 1000)}ms',
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):
    await bot.add_cog(Geral(bot))
