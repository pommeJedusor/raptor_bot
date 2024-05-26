import discord
from discord.ext import commands

import datas as Datas


cogs = [
]


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    try:
        for cog in cogs:
            await bot.load_extension(f"cogs.{cog}")

        synced = await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    bot.run(Datas.bot_token)
