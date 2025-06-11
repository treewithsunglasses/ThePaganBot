"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.3.0
"""

import random

import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import Context


class Fun(commands.Cog, name="fun"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name="coinflip", description="Flip a coin!")
    async def coinflip(self, context: Context) -> None:
        """
        Flips a coin!

        :param context: The hybrid command context.
        """
        embed = discord.Embed(title=random.choice(["Heads", "Tails"]), color=0xD75BF4)
        await context.send(embed=embed)


async def setup(bot) -> None:
    await bot.add_cog(Fun(bot))
