import discord
from discord.ext import commands
from discord import app_commands
import json
import time

bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

@bot.event
async def on_ready():
    try:
        s = await bot.tree.sync()
        print(f'Synced {len(s)} commands')
    except Exception as e:
        print(f'Error syncing commands: {e}')
    
    print(f'Logged in as {bot.user.name}')
    
@bot.tree.command(name='hello', description='Hello World!')
async def hello(interaction: discord.Interaction):
    # Send a message:
    await interaction.response.send_message('Hello World!')
    
@bot.tree.command(name='ping', description='Display the latency of the bot!')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! ||{round(bot.latency * 1000)}ms||')
    
@bot.tree.command(name='say', description='I\'ll repeat what you want to say!')
@app_commands.describe(what_to_say='The message you want me to say!')
async def say(interaction: discord.Interaction, what_to_say: str):
    await interaction.response.send_message(f'{what_to_say} - **{interaction.user.display_name}**')
    
@bot.tree.command(name='defer_response', description='I\'ll reply after a period of time!')
async def defer_response(interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.followup.send('Waiting...')
    time.sleep(10)
    await interaction.edit_original_response(content='Replying after 10 seconds!')
    
token = config['token']
bot.run(token)