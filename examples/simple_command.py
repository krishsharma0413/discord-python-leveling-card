# example made with pycord
import discord
from discord.ext import commands
from discord.ext.commands.context import Context

from DiscordLeveling import level_maker

client = commands.Bot(command_prefix='!')


@client.command()
async def level(message, user:discord.Member=None):
    user = user or message.author
    backgound = "link to some image"
    avatar = user.display_avatar.url
    level = 25
    current_exp = 1000
    max_exp = 3000
    bar_color = "#00ffef"
    a = await level_maker(backgound,avatar,user.display_name,current_exp,level,max_exp,bar_color)
    await message.channel.send(file=discord.File(a))


client.run("your bot token")
