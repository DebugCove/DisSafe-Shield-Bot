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

@bot.tree.command(name='ban', description='Ban a user')
@app_commands.checks.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str):
    try:
        await member.ban(reason=reason)
        embed = discord.Embed(
            title='Ban',
            description=f'{member} was banned. Reason: {reason}',
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
    except Exception as error:
        embed = discord.Embed(
            title='Ban',
            description=f'Error banning {member.mention}',
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        print(f'There was an error banning the user {member} the reason would be {reason}\nError {error}')



load_dotenv()
TOKEN = getenv('TOKEN')
bot.run(TOKEN)
