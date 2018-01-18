import discord
from discord.ext import commands
from random import choice, randint
import re


def process_avatar(url):
    if ".gif" in url:
        new_url = url + "&f=.gif"
        return new_url
    else:
        new_url = url.replace('.webp', '.png')
        return new_url


class Avatar:
    """Get user's avatar URL."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def avatar(self, ctx, *, user: discord.Member=None):
        """Returns user avatar URL."""
        author = ctx.message.author

        if not user:
            user = author

        u = user.avatar_url
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        randnum = randint(1, 10)
        empty = u"\u2063"
        emptyrand = empty * randnum
        url = process_avatar(u)
        if url:
            data = discord.Embed(title="Direct Link", url=url, colour=discord.Colour(value=colour))
            data.set_image(url=url)
        if user:
            data.set_author(name=user.name)
        else:
            data.set_author(name=author.name)
        try:
            await self.bot.say(emptyrand, embed=data)
        except:
            await self.bot.say("Try giving me permission to embed links.")


def setup(bot):
    bot.add_cog(Avatar(bot))
