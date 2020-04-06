import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
hus_responses = []

@client.event
async def on_ready():
    print('Cock is ready.')

@client.command(help='Check ping to server.')
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(help='Got cocked!')
async def huso(ctx):
    await ctx.send(f'{random.choice(hus_responses)}')

@client.command(help='Add a nur huso response. Example: .add_huso This is the new huso!')
async def add_huso(ctx, *args):
    slur = " ".join(args)
    if isinstance(slur, str) and len(slur) < 140:
        hus_responses.append(slur)
        # persistent save
        with open('huso-data.txt', 'a') as fp:
            fp.write(slur + '\n')
        await ctx.send(f'{ctx.author} added new huso: {slur}')
    else:
        await ctx.send(f'ERROR Could not add new huso (no string or too long): {slur}')


if __name__ == '__main__':
    print("Preparing bot. Loading data.")

    with open('huso-data.txt', 'r') as fp:
        for line in fp.readlines():
            if len(line)>0:
                hus_responses.append(line)
               
    
    client.run('')
