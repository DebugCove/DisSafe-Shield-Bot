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
    if member == interaction.guild.me:
        embed = discord.Embed(
            title='Ban Error',
            description="I cann't ban myself.",
            color=discord.Color.red()
        )
        return await interaction.response.send_message(embed=embed, ephemeral=True)

    if member == interaction.user:
        embed = discord.Embed(
            title='Ban Error',
            description="You can't ban yourself.",
            color=discord.Color.red()
        )
        return await interaction.response.send_message(embed=embed, ephemeral=True)

    if member.top_role >= interaction.user.top_role:
        embed = discord.Embed(
            title='Ban Error',
            description="You can't ban this user because they have a position equal to or higher than yours",
            color=discord.Color.red()
        )
        return await interaction.response.send_message(embed=embed, ephemeral=True)

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

@bot.tree.command(name='mute', description='Mute a user')
@app_commands.checks.has_permissions(manage_roles=True)
async def mute(interaction: discord.Interaction, member: discord.Member, reason: str, duration: int = None):
    if member == interaction.guild.me:
        embed = discord.Embed(
            title='Ban Error',
            description="I cann't mute myself.",
            color=discord.Color.red()
        )
        return await interaction.response.send_message(embed=embed, ephemeral=True)

    if member == interaction.user:
        embed = discord.Embed(
            title='Ban Error',
            description="You can't mute yourself.",
            color=discord.Color.red()
        )
        return await interaction.response.send_message(embed=embed, ephemeral=True)

    if member.top_role >= interaction.user.top_role:
        embed = discord.Embed(
            title='Ban Error',
            description="You can't mute this user because they have a position equal to or higher than yours",
            color=discord.Color.red()
        )
        return await interaction.response.send_message(embed=embed, ephemeral=True)

    mute_role = discord.utils.get(interaction.guild.roles, id=1214179278296584232)
    if not mute_role:
        await interaction.response.send_message("Cargo 'Muted' não encontrado.", ephemeral=True)
        return

    await member.add_roles(mute_role, reason=reason)
    message = f'{member.mention} foi silenciado'
    if duration:
        message += f' por {duration} minutos'
    message += f'. Motivo: {reason}'
    await interaction.response.send_message(message)

    if duration:
        await asyncio.sleep(duration * 60)
        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            await interaction.followup.send(f'{member.mention} foi desmutado automaticamente após {duration} minutos.', ephemeral=True)



load_dotenv()
TOKEN = getenv('TOKEN')
bot.run(TOKEN)
