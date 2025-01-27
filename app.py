from os import getenv
from dotenv import load_dotenv
import nextcord
from nextcord import Interaction, ChannelType
from nextcord.ext import commands
from nextcord.ui import Button, View


load_dotenv()
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is online and ready to use!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping {round(bot.latency * 1000)}ms')


TOKEN = getenv('TOKEN')
if TOKEN is None:
    raise Exception('TOKEN is not set')

bot.run(TOKEN)
