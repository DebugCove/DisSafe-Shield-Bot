import asyncio
from datetime import datetime, timedelta, timezone
from os import getenv
from dotenv import load_dotenv

import nextcord
from nextcord import Interaction, ChannelType
from nextcord.ext import commands, tasks
from nextcord.ui import Button, View

from config.config import create_config_file
from extras.logs import send_logs_guild, send_logs_debug

load_dotenv()
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
IP_API = getenv('API_URL')


@bot.event
async def on_ready():
    print(f'{bot.user} is online and ready to use!')


@bot.event
async def on_guild_join(guild):
    print(f'\U0001F389 The bot entered the server: {guild.name} (ID: {guild.id})')
    create_config_file(guild.id)


@bot.slash_command(description='See bot latency')
async def ping(interaction: Interaction):
    await interaction.followup.send(f'Ping: {round(bot.latency * 1000)}ms', ephemeral=True)


@bot.slash_command(description='Make a user report')
async def make_report(
    interaction: Interaction,
    user: nextcord.User,
    reason: str,
    proof: str,
    accuser: nextcord.User = None
):
    await interaction.response.defer(ephemeral=True)
    if user == interaction.user:
        await interaction.followup.send('You cannot report yourself.', ephemeral=True)
        return
    
    if user == bot.user:
        await interaction.followup.send('You cannot report the bot.', ephemeral=True)
        return

    accuser = accuser or interaction.user
    guild = interaction.guild
    if user.bot:
        result_bot = 'Yes'
    result_bot = 'No'

    embed = nextcord.Embed(
        title='Report Sent',
        description=(
            f'**User:** {user.mention}\n'
            f'**Reason:** {reason}\n'
            f'**Proof:** {proof}\n'
            f'**Bot:** {result_bot}\n'
            f'**Accuser:** {accuser.mention}'
        ),
        color=nextcord.Color.green()
    )
    embed.set_footer(
        text=f'Reported by: {interaction.user.display_name} | Server: {guild.id}',
        icon_url=interaction.user.display_avatar.url
    )

    await send_logs_guild(interaction, bot, guild.id, embed)
    await send_logs_debug(interaction, bot, embed)
    await interaction.followup.send('Report made successfully!', ephemeral=True)


try:
    TOKEN = getenv('TOKEN')
    if not TOKEN:
        raise ValueError('TOKEN is not set.')
    bot.run(TOKEN)
except Exception as error:
    print(f'Error starting bot: {error}')
