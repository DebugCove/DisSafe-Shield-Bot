from os import getenv
from dotenv import load_dotenv
import asyncio
import discord
from discord import app_commands
from discord.ext import commands


INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix=None, intents=INTENTS)


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f'\n\nSicronised {len(synced)} slash commands.')
    except Exception as error:
        print(f'\n\nError when synchronising commands\n{error}')
    print(f'Bot connect with {bot.user.name}\n\n')

@bot.tree.command(name='ping', description='Show the bot latency')
async def ping(interaction: discord.Interaction):
    embed = discord.Embed(
        title='Pong!',
        description=f'Bot latency: {round(bot.latency * 1000)}ms',
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)



load_dotenv()
TOKEN = getenv('TOKEN')
bot.run(TOKEN)
