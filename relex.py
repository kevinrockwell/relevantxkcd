import os

import asyncio
import random
import re
from discord.ext import commands
from dotenv import load_dotenv
from googlesearch import search

from newest_xkcd import latest_comic_num

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

URL = 'https://xkcd.com/'


bot = commands.Bot(command_prefix='!')

@bot.command(name='number', pass_context=True)
async def number(ctx, number):
    await ctx.send(f'{URL}{number}/')

@bot.command(name='random_comic', pass_context=True)
async def random_comic(ctx):
    newest_comic = latest_comic_num()
    comic_num = random.randint(1, newest_comic)
    await ctx.send(f'{URL}{comic_num}/')

@bot.command(name='phrase', pass_context=True)
async def phrase(ctx, phrase):
    query = f'site:xkcd.com {str(phrase)}'
    pattern = r'^https?://xkcd.com/\d+/$'
    first = -1
    found = False
    while found == False:
        first+= 1
        result = search(query, num=1, start=first, pause=2.0)
        if re.match(pattern, result):
            found = True
    await ctx.send(result)

bot.run(TOKEN)

