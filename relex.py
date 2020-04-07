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

@bot.command(name='search_phrase', pass_context=True)
async def search_phrase(ctx, phrase):
    query = f'site:xkcd.com {str(phrase)}'
    pattern = r'^https?://xkcd.com/\d+/$'
    found = False
    link = ''
    first = -1
    last = 0
    links = 0
    await ctx.send(f'Now searching for the xkcd most relevant to the phrase \"{phrase}\".')
    while found == False:
        first += 1
        last += 1
        if links >= 10:
            await ctx.send('I searched through 10 links and didn\'t find a match. Maybe there\'s not always a relevant xkcd.')
            return
        result = search(query, num=10, start=first, stop=last, pause=2.0)
        for page in result:
            links += 1
            if re.match(pattern, page):
                link = page
                found = True
    await ctx.send(f'The most relevant xkcd found for the phrase \"{phrase}\" is {link}')

bot.run(TOKEN)

