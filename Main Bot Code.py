import discord
from discord.ext import commands
import asyncio
import time
import pathlib
import os
import Fancy_Necklaces
import Season_Functions
import Accessories
import Outfit_Pictures
client = commands.Bot(command_prefix = "ootd")
client.remove_command("help")



#Gender function definitions
async def girl(ctx, cli):
    gender = "girl"
    channel = ctx.channel
    SpringOrSummerEmoji = "\U0001F33B"
    WinterEmoji = "\u2744"
    AutumnEmoji = "\U0001F383"
    await ctx.send("You chose girl!")
    message = await ctx.send("What season would you like your outfit to fit? \n:sunflower: = 'Spring/Summer \n:snowflake: = 'Winter' \n:jack_o_lantern: = 'Autumn'")
    await message.add_reaction(SpringOrSummerEmoji)
    await message.add_reaction(WinterEmoji)
    await message.add_reaction(AutumnEmoji)
    def check(reaction, user):
        return user != message.author and (str(reaction.emoji) == SpringOrSummerEmoji or str(reaction.emoji) == AutumnEmoji or str(reaction.emoji) == WinterEmoji)
    try:
        reaction, user = await client.wait_for("reaction_add", check=check, timeout=60.0)

    except asyncio.TimeoutError:
        await ctx.send("you left me on read :(")

    if str(reaction.emoji) == SpringOrSummerEmoji:
        await ctx.send(user)
        await Season_Functions.SpringOrSummer(ctx, gender, cli)
    elif str(reaction.emoji) == AutumnEmoji:
        await ctx.send(user)
        await Season_Functions.autumn(ctx, gender, cli)
    elif str(reaction.emoji) == WinterEmoji:
        await ctx.send(user)
        await Season_Functions.winter(ctx, gender, cli)

async def boy(ctx, cli):
    await ctx.send("You chose boy!")
    gender = "boy"
    channel = ctx.channel
    SpringOrSummerEmoji = "\U0001F33B"
    WinterEmoji = "\u2744"
    AutumnEmoji = "\U0001F383"
    message = await ctx.send("What season would you like your outfit to fit? \n:sunflower: = 'Spring/Summer \n:snowflake: = 'Winter' \n:jack_o_lantern: = 'Autumn'")
    await message.add_reaction(SpringOrSummerEmoji)
    await message.add_reaction(WinterEmoji)
    await message.add_reaction(AutumnEmoji)
    def check(reaction, user):
        return user != message.author and (str(reaction.emoji) == SpringOrSummerEmoji or str(reaction.emoji) == AutumnEmoji or str(reaction.emoji) == WinterEmoji)
    try:
        reaction, user = await cli.wait_for("reaction_add", check=check, timeout=60.0)

    except asyncio.TimeoutError:
        await ctx.send("you left me on read :(")

    if str(reaction.emoji) == SpringOrSummerEmoji:
        await ctx.send(user)
        await Season_Functions.SpringOrSummer(ctx, gender, cli)
    elif str(reaction.emoji) == AutumnEmoji:
        await ctx.send(user)
        await Season_Functions.autumn(ctx, gender, cli)
    elif str(reaction.emoji) == WinterEmoji:
        await ctx.send(user)
        await Season_Functions.winter(ctx, gender, cli)

async def neutral(ctx, cli):
    gender = "neutral"
    await ctx.send("You chose neutral!")
    SpringOrSummerEmoji = "\U0001F33B"
    WinterEmoji = "\u2744"
    AutumnEmoji = "\U0001F383"
    message = await ctx.send("What season would you like your outfit to fit? \n:sunflower: = 'Spring/Summer \n:snowflake: = 'Winter' \n:jack_o_lantern: = 'Autumn'")
    await message.add_reaction(SpringOrSummerEmoji)
    await message.add_reaction(WinterEmoji)
    await message.add_reaction(AutumnEmoji)

    def check(reaction, user):
        return user != message.author and (str(reaction.emoji) == SpringOrSummerEmoji or str(reaction.emoji) == AutumnEmoji or str(reaction.emoji) == WinterEmoji)

    try:
        reaction, user = await cli.wait_for("reaction_add", check=check, timeout=60.0)

    except asyncio.TimeoutError:
        await ctx.send("you left me on read :(")

    if str(reaction.emoji) == SpringOrSummerEmoji:
        await ctx.send(user)
        await Season_Functions.SpringOrSummer(ctx, gender, cli)
    elif str(reaction.emoji) == AutumnEmoji:
        await ctx.send(user)
        await Season_Functions.autumn(ctx, gender, cli)
    elif str(reaction.emoji) == WinterEmoji:
        await ctx.send(user)
        await Season_Functions.winter(ctx, gender, cli)







@client.event
async def on_ready():
    print("We have logged in as " + str(client.user))
    game = discord.Game("type 'ootdhelp' or 'ootd-help'")
    await client.change_presence(activity=game, status=discord.Status.online, afk=False)

@client.command(aliases=['-help'])
async def help(ctx):
    await ctx.send("Command Prefix: 'ootd' or 'ootd-' \nCommands include: 'outfit', 'accessory', 'all', 'shoes' \nNotes: You can use - after the prefix when calling a command to make it easier to read.")

@client.command(aliases = ['-outfit'])
async def outfit(ctx):
    await ctx.send("Let the OOTD generator help you find the perfect outfit for today!")
    message = await ctx.send("What gender of outfit would you like? Girl, Boy, Neutral\n")
    GirlEmoji = '\U0001F467'
    BoyEmoji =  '\U0001F466'
    NeutralEmoji = '\u2194'
    await message.add_reaction(GirlEmoji)
    await message.add_reaction(BoyEmoji)
    await message.add_reaction(NeutralEmoji)
    def check(reaction, user):
        return user != message.author and (str(reaction.emoji) == GirlEmoji or str(reaction.emoji) == BoyEmoji or str(reaction.emoji) == NeutralEmoji)
    try:
        reaction, user = await client.wait_for('reaction_add', check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await ctx.send("you left me on read :(")

    if str(reaction.emoji) == GirlEmoji:
        await girl(ctx, client)
    elif str(reaction.emoji) == BoyEmoji:
        await boy(ctx, client)
    elif str(reaction.emoji) == NeutralEmoji:
        await neutral(ctx, client)

@client.command(aliases=['-accessory', 'accessories', '-accessories'])
async def accessory(ctx):
    channel = ctx.channel
    await ctx.send("What accessory would you like? Necklace, Ring, Hat")
    def check(m):
        return m.channel == channel and (m.content.lower() == "necklace" or m.content.lower() == "ring" or m.content.lower() == "hat")
    thing = await client.wait_for("message", check=check, timeout=60.0)

    if thing.content.lower() == "necklace":
        item = "necklace"
    elif thing.content.lower() == "ring":
        item = "ring"
    elif thing.content.lower() == "hat":
        item = "hat"

    await ctx.send("What style would you like? Fancy, Casual, Cute")
    def check(m):
        return m.channel == channel and (m.content.lower() == "fancy" or m.content.lower() == "casual" or m.content.lower() == "cute")
    style_msg = await client.wait_for("message", check=check, timeout=60.0)

    if style_msg.content.lower() == "fancy":
        style = "fancy"
    elif style_msg.content.lower() == "casual":
        style = "casual"
    elif style_msg.content.lower() == "cute":
        style = "cute"

    await Accessories.accessory(ctx, client, item, style)


@client.command(aliases = ['-shoes'])
async def shoes(ctx):
    await ctx.send("What style of shoe would you like? \nFancy, Casual, Sporty")
    def check(m):
        return m.channel == ctx.channel and (m.content.lower() == "fancy" or m.content.lower() == "casual" or m.content.lower() == "sporty")

    which_style = await client.wait_for("message", check=check, timeout=70.0)
    if which_style.content.lower() == "fancy":
        style = "fancy"
    elif which_style.content.lower() == "casual":
        style = "casual"
    elif which_style.content.lower() == "sporty":
        style = "sporty"

    await Accessories.shoes(ctx,client,style)


@client.command(aliases = ['-all'])
async def all(ctx):
    index = 0
    Outfits = os.listdir(path='Outfit_Pictures')
    going = True
    scroll = "\U0001F4DC"
    play_button = "\u25B6"
    next = "\u27A1"
    back = "\u2B05"
    stop = "\U0001F6D1"

    whichone = await ctx.send("Would you like to see the list of outfits or a slideshow of them? \n:scroll: = list \n:arrow_forward: = slideshow")
    await whichone.add_reaction(scroll)
    await whichone.add_reaction(play_button)

    def check(reaction, user):
        return user != whichone.author and (str(reaction) == scroll or str(reaction) == play_button)

    reaction, user = await client.wait_for('reaction_add', check=check, timeout=60.0)

    if str(reaction) == scroll:
        Numbered_Outfits = []
        for i in range(len(Outfits)):
            Numbered_Outfits.append(str(i + 1) + ". " + Outfits[i])

        await ctx.send("\n".join(Numbered_Outfits))

        await ctx.send("**Type which number you want to see**")
        def check(m):
            return m.channel == ctx.channel and int(m.content) <= len(Outfits)

        number = await client.wait_for("message", check=check, timeout=60.0)
        number = int(number.content)
        which_file = Outfits[number - 1]
        await ctx.send(which_file)
        await ctx.send(file=discord.File("Outfit_Pictures/" + which_file))


    elif str(reaction) == play_button:
        warning = await ctx.send(":octagonal_sign: = deletes the image")
        while going:

            name = await ctx.send(Outfits[index])
            pic = await ctx.send(file=discord.File("Outfit_Pictures/" + Outfits[index]), delete_after=120.0)
            await pic.add_reaction(back)
            await pic.add_reaction(stop)
            await pic.add_reaction(next)

            def check(reaction, user):
                return user != pic.author and (str(reaction) == next or str(reaction) == stop or str(reaction) == back)

            try:
                reaction, user = await client.wait_for('reaction_add', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                going = False

            if str(reaction) == next:
                await name.delete()
                await pic.delete()
                if index != len(Outfits) - 1:
                    index = index + 1
                else:
                    await ctx.send("That's the end")
                    index = index
            elif str(reaction) == back:
                await name.delete()
                await pic.delete()
                index -= 1
            elif str(reaction) == stop:
                await name.delete()
                await pic.delete()
                await warning.delete()
                going = False



secret = open("token.txt")
token = secret.read()
secret.close()
client.run(token)

