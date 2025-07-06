from dotenv import load_dotenv
from os import getenv
from discord.ext import commands
import discord
import asyncio


load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = getenv('TOKEN')

async def load_cogs():
    await bot.load_extension('cogs.geral')
    await bot.load_extension('cogs.events')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    exit()
except Exception as e:
    print(f'An error occurred: {e}')
    exit(1)
