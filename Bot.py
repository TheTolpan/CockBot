import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Cock is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def huso(ctx):
    responses = ['Bist du behindert?',
                 'Amina Sikerim!',
                 'Selbst Lars würde dich beleidigen.',
                 'Selbst Dobos Mutter würde dich von der Bettkante schupsen.']
    await ctx.send(f'{random.choice(responses)}')

client.run('')
