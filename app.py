from nextcord import Interaction, ChannelType
from nextcord.ext import commands, tasks
from nextcord.ui import Button, View
import nextcord

from os import getenv
from dotenv import load_dotenv
from config.main import load_config
import logging
import logging.config


load_dotenv()
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('logs_bot')
config = load_config()
prefix = config['service']['bot']['prefix']
if prefix is None or not isinstance(prefix, str):
    logger.info('Prefix not defined in settings use default "!"')
    prefix = '!'

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    logger.info(f'Bot {bot.user} is online and ready to use!')  

@bot.slash_command(description='See bot latency')
async def ping(interaction: Interaction):
    await interaction.response.defer(ephemeral=True)
    await interaction.followup.send(f'Ping: {round(bot.latency * 1000)}ms', ephemeral=True)


try:
    TOKEN = getenv('TOKEN')
    if not TOKEN or not isinstance(TOKEN, str):
        logger.error('token has not been defined or is invalid')
        exit(1)
    bot.run(TOKEN)
except Exception as error:
    logger.error(f'Error when trying to run the bot check if the token is invalid: {error}')
    exit(1)