import nextcord
from config.config import load_config, load_server_config


async def send_logs_guild(interaction, bot, guild, embed):
    print(f'Logs guild {guild}')
    config = load_server_config(guild)
    if config is None:
        print('Config is none')
        await interaction.response.send_message('Erro try send log', ephemeral=True)
        return

    chat_logs = config['chat_logs_id']
    if chat_logs is None:
        print('Chat logs is none')
        await interaction.response.send_message('Erro try send log', ephemeral=True)
        return

    guild = bot.get_guild(guild)
    if guild is None:
        print('Guild is none')
        await interaction.response.send_message('Erro try send log', ephemeral=True)
        return

    channel = guild.get_channel(chat_logs)
    if channel is None:
        print('Channel is none')
        await interaction.response.send_message('Erro try send log', ephemeral=True)
        return

    await channel.send(embed=embed)


async def send_logs_debug(interaction, bot, embed):
    print('Logs Debug Cove')
    config = load_config()
    if config is None:
        print('Config is none')
        await interaction.response.send_message('Erro try send log', ephemeral=True)
        return

    chat_logs = config['chat_logs_id']
    if chat_logs is None:
        print('Chat logs is none')
        await interaction.response.send_message('Erro try send log', ephemeral=True)
        return

    channel = bot.get_channel(chat_logs)
    if channel is None:
        print('Channel is none')
        await interaction.response.send_message('Erro try send log', ephemeral=True)
        return

    await channel.send(embed=embed)