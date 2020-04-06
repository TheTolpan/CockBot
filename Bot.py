import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
huso_repsonses = []

@client.event
async def on_ready():
    print('Cock is ready.')

@client.command(help='Check ping to server.')
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(help='Got cocked!')
async def huso(ctx):
    await ctx.send(f'{random.choice(huso_repsonses)}')

@client.command(help='Add a nur huso response. Example: .add_huso This is the new huso!')
async def add_huso(ctx, slur):
    if isinstance(slur, str) and len(slur) < 140:
        huso_repsonses.append(slur)
        # persistent save
        with open('huso-data.txt', 'w') as fp:
            fp.write(slur + '\n')
        await ctx.send(f'{ctx.author} added new huso: {slur}')
    else:
        await ctx.send(f'ERROR Could not add new huso (no string or too long): {slur}')


if __name__ == '__main__':
    print("Preparing bot. Loading data.")

    with open('huso-data.txt', 'r') as fp:
        for line in fp.readlines():
            if len(line)>0:
                huso_repsonses.append(line)
               
    
    client.run('')
