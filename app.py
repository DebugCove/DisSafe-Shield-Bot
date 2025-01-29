from os import getenv
from dotenv import load_dotenv
import nextcord
from nextcord import Interaction, ChannelType
from nextcord.ext import commands
from nextcord.ui import Button, View
from config.config import create_config_file
from config.config import load_config


load_dotenv()
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is online and ready to use!')

@bot.event
async def on_guild_join(guild):
    config = load_config()
    id_debug_cove = config.get('server_id')
    id_channel_logs_debug_cove = config.get('chat_logs_id')

    print(f"🎉 The bot entered the server: {guild.name} (ID: {guild.id})")
    create_config_file(guild.id)

    guild_debug_cove = bot.get_guild(int(id_debug_cove))
    if guild_debug_cove:
        log_channel_debug_cove = guild_debug_cove.get_channel(int(id_channel_logs_debug_cove))
        if log_channel_debug_cove:
            embed = nextcord.Embed(
                title='Bot was added in new server'
                description=(
                    f'Bot was added to a new server\n'
                    f'Server name: {guild.name}\n'
                    f'Server ID: {guild.id}'
                ),
                color=nextcord.Color.blue()
            )
            await log_channel_debug_cove.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping {round(bot.latency * 1000)}ms')



TOKEN = getenv('TOKEN')
if TOKEN is None:
    raise Exception('TOKEN is not set')

bot.run(TOKEN)
