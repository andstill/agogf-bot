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
    await channel.send("""Redacted for git commit""")
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
    $delrole [role] - Deletes the role.
    $delchannel [channel] - Deletes the channel.
    $muteau - Mutes the designated Among Us channel.
    $unmuteau - Unmutes everybody in the designated Among Us channel.
    $muteraid - Mutes the designated Raid channel.
    $unmuteraid - Unmutes the designated Raid channel.
    $mplus - Links to a website of all-knowing m+
    $privchan - Creates a private channel with officers and the user in question.
    $help - Displays an automated help message.

    $cmd - List this menu you're reading right now.
    $botup - A simple check to see if I am up and operational. $help and $cmd also works.

----------------------------

The following commands are not-yet implemented, though planned:
    $token - Fetch the price of a token in US.
    $rio [player] - Fetch the general raider.io score of a character.

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
        await role.delete()
        await ctx.send("The role and channel was deleted.")
    else:
        await ctx.send("Owner of the discord did not write the command. Ignoring.")
    return

@bot.command(pass_context=True)
async def delchannel(ctx, channel: discord.TextChannel):
    if str(ctx.author) == owner:
        await channel.delete()
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

