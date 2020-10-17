import discord
import random
import asyncio
import discord.utils
import time
import dotenv
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORDTOKEN')
owner = os.getenv('OWNER')
raid = os.getenv('RAID_CHANNEL')
amongus = os.getenv('AMONGUS_CHANNEL')
officer = os.getenv('OFFICER_CHANNEL')
officerrole = os.getenv('OFFICER_ROLE')
bot = commands.Bot(command_prefix="$")

@bot.event
async def on_member_join(ctx):
    name = ctx.display_name
    guild = ctx.guild
    category = discord.utils.get(ctx.guild.categories, name="Applications")
    role = await guild.create_role(name=name)
    officer = discord.utils.get(ctx.guild.roles, name="Officer")
    founder = discord.utils.get(ctx.guild.roles, name="Founder")
    roles = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        officer: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True),
        role: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True),
        founder: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True)
    }
    channel = await guild.create_text_channel(name, overwrites=roles, category=category)
    selfrole = discord.utils.get(ctx.guild.roles, name=name)
    await ctx.add_roles(selfrole)
    time.sleep(5)
    await channel.send("""here Hello, newcomer! Welcome to the <A Group of Good Friends> Discord server!
    This channel you were just pinged in is private -- Only specific people of the guild (Officers, GM, and yourself) are actually able to see this message, as we intend to use this channel for your application process. You can post your application in this channel and we'll interacting with your privately in this channel. You're more than welcome to talk to anyone in the guild in any channel available to you, but anything related to recruitment will probably be kept here.

**__How to proceed:__**
    Fill out the questions posted below, they aren't too serious and if you don't think you have a good answer for one then still answer it. This isn't a cut-throat job application, it's just important information we're gathering for recruitment for now.
```--What's your previous raiding experience? If it was just heroic, that's fine, but we want to know:
--This guild is entirely focused on achieving Cutting Edge every tier plus ample time to farm it. This obviously requires a certain amount of dedication and a relatively competitive mindset from everyone in the guild, but we're not elitist about it. Do you think your goals line up with ours?
--What role are you primarily interested in, and with that your main and any alts?
--Is there any warcraftlogs or raider.io you can give of anyone current? If not, that's fine!

        FUN QUESTIONS
--What's your favorite raid and your favorite raid boss in WoW?
--Outside of WoW, what games do you enjoy playing? This group is having a ton of fun with Among Us and Counter-Strike lately. Interested in either of these games?
--Funniest video(s) you've seen on the internet recently, we want to see them. NSFW is totally allowed:```
Again, we appreciate your interest and we'll be responding to you ASAP! Feel free to add any information or ask us any questions in the mean time.""")
    return

@bot.event
async def on_member_remove(ctx):
    name = ctx.display_name
    guild = ctx.guild
    selfrole = discord.utils.get(ctx.guild.roles, name=name)
    selfchannel = discord.utils.get(ctx.guild.channels, name=name)
    officerchannel = discord.utils.get(ctx.guild.channels, name=officer)
    await officerchannel.send("The member: " + str(name) + ", has left the discord. I've cleaned up their personal channel and role (if applicable).")
    if selfchannel is not None:
        await selfchannel.delete()
    if selfrole is not None:
        await selfrole.delete()
    return

@bot.command(pass_context=True)
async def cmd(ctx):
    await ctx.send("""
    ```The following commands are what I have been programmed to respond to:
    $delrole [role] - Deletes the role and channel of a user.
    $muteau - Mutes the designated Among Us channel.
    $unmuteau - Unmutes everybody in the designated Among Us channel.
    $muteraid - Mutes the designated Raid channel.
    $unmuteraid - Unmutes the designated Raid channel.
    $mplus - Links to a website of all-knowing m+

    $cmd - List this menu you're reading right now.
    $botup - A simple check to see if I am up and operational. $help and $cmd also works.

----------------------------

The following commands are not-yet implemented, though planned:
    $token - Fetch the price of a token in US.
    $rio [player] - Fetch the general raider.io score of a character.
    $privchan - Create a private test channel between the author and officers.

----------------------------

Additionally, I have some fun commands I run in the background when people join and leave the discord automagically.```""")
    return

@bot.command(pass_context=True)
async def botup(ctx):
    await ctx.send("Bot is up and operational.")
    return

@bot.command(pass_context=True)
async def privchan(ctx):
    name = ctx.message.author.name
    guild = ctx.guild
    category = discord.utils.get(ctx.guild.categories, name="Private Channels")
    role = await guild.create_role(name=name)
    officer = discord.utils.get(ctx.guild.roles, name="Officer")
    roles = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        officer: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True),
        role: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True)
    }
    channel = await guild.create_text_channel(name, overwrites=roles, category=category)
    await ctx.message.author.add_roles(role)
    time.sleep(3)
    await channel.send("@here A user requested a private channel with the officers. Creating.")
    return

@bot.command(pass_context=True)
async def mplus(ctx):
    await ctx.send("For current affixes and weekly rotation: https://mythicpl.us/")
    return

@bot.command(pass_context=True)
async def muteau(ctx):
    toprole = discord.utils.get(ctx.guild.roles, name=officerrole)
    if toprole in ctx.author.roles:
        vchan = discord.utils.get(ctx.guild.channels, name=amongus)
        for member in vchan.members:
            await member.edit(mute=True)
    else:
        await ctx.send("Officer of the discord did not write the command. Ignoring.")
    return

@bot.command(pass_context=True)
async def unmuteau(ctx):
    toprole = discord.utils.get(ctx.guild.roles, name=officerrole)
    if toprole in ctx.author.roles:
        vchan = discord.utils.get(ctx.guild.channels, name=amongus)
        for member in vchan.members:
            await member.edit(mute=False)
    else:
        await ctx.send("Officer of the discord did not write the command. Ignoring.")
    return

@bot.command(pass_context=True)
async def muteraid(ctx):
    toprole = discord.utils.get(ctx.guild.roles, name=officerrole)
    if toprole in ctx.author.roles:
        vchan = discord.utils.get(ctx.guild.channels, name=raid)
        for member in vchan.members:
            await member.edit(mute=True)
    else:
        await ctx.send("Officer of the discord did not write the command. Ignoring.")
    return

@bot.command(pass_context=True)
async def unmuteraid(ctx):
    toprole = discord.utils.get(ctx.guild.roles, name=officerrole)
    if toprole in ctx.author.roles:
        vchan = discord.utils.get(ctx.guild.channels, name=raid)
        for member in vchan.members:
            await member.edit(mute=False)
    else:
        await ctx.send("Officer of the discord did not write the command. Ignoring.")
    return

@bot.command(pass_context=True)
async def delrole(ctx, role: discord.Role):
    if str(ctx.author) == owner:
        guild = ctx.guild
        selfchannel = discord.utils.get(ctx.guild.channels, name=role)
        officerchannel = discord.utils.get(ctx.guild.channels, name=officer)
        await role.delete()
        await ctx.send("The role and channel was deleted.")
    if str(ctx.author) != owner:
        await ctx.send("Owner of the discord did not write the command. Ignoring.")
    return

@bot.command(pass_context=True)
async def delchannel(ctx, channel_name):
    if str(ctx.author) == owner:
        await bot.delete_channel("channel_name")
        await ctx.send("Channel deleted.")
    else:
        await ctx.send("Owner of the discord did not write the command. Ignoring.")
    return

@delchannel.error
async def info_error (ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("The channel doesn't exist. No action taken.")
    return

@delrole.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("The role does not exist.")
    return

bot.run(token)
