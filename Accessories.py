import discord
from discord.ext import commands
import asyncio
import time
import os
import Fancy_Necklaces
import Casual_Necklaces
import Cute_Necklaces
import Fancy_Rings
import Casual_Rings
import Cute_Rings
import Fancy_Hats
import Casual_Hats
import Cute_Hats

# Items: necklace, ring, hat
# Styles: fancy, casual, cute
async def accessory(ctx, cli, item, style):
    next = "\u27A1"
    back = "\u2B05"
    stop = "\U0001F6D1"

    await ctx.send("You chose " + item + " with the style of " + style)
    if item == "necklace":
        if style == "fancy":
            Fancy_Necks = os.listdir(path="Fancy_Necklaces")
            going = True
            index = 0
            while going:
                pic = await ctx.send(file=discord.File("Fancy_Necklaces/" + Fancy_Necks[index]), delete_after=120.0)
                await pic.add_reaction(back)
                await pic.add_reaction(stop)
                await pic.add_reaction(next)

                def check(reaction, user):
                    return user != pic.author and (str(reaction) == next or str(reaction) == stop or str(reaction) == back)

                try:
                    reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
                except asyncio.TimeoutError:
                    going = False

                if str(reaction) == next:
                    await pic.delete()
                    if index != len(Fancy_Necks) - 1:
                        index = index + 1
                    else:
                        await ctx.send("That's the end")
                        index = index
                elif str(reaction) == back:
                    await pic.delete()
                    index = index - 1
                elif str(reaction) == stop:
                    await pic.delete()
                    going = False

        elif style == "casual":
            going = True
            index = 0
            while going:
                Casual_Necks = os.listdir(path="Casual_Necklaces")
                pic = await ctx.send(file=discord.File("Casual_Necklaces/" + Casual_Necks[index]), delete_after=120.0)
                await pic.add_reaction(back)
                await pic.add_reaction(stop)
                await pic.add_reaction(next)

                def check(reaction, user):
                    return user != pic.author and (str(reaction) == next or str(reaction) == stop or str(reaction) == back)

                try:
                    reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
                except asyncio.TimeoutError:
                    going = False

                if str(reaction) == next:
                    await pic.delete()
                    if index != len(Casual_Necks) - 1:
                        index = index + 1
                    else:
                        await ctx.send("That's the end")
                        index = index
                elif str(reaction) == back:
                    await pic.delete()
                    index = index - 1
                elif str(reaction) == stop:
                    await pic.delete()
                    going = False

        elif style == "cute":
            going = True
            index = 0
            while going:
                Cute_Necks = os.listdir(path="Cute_Necklaces")
                pic = await ctx.send(file=discord.File("Cute_Necklaces/" + Cute_Necks[index]), delete_after=120.0)
                await pic.add_reaction(back)
                await pic.add_reaction(stop)
                await pic.add_reaction(next)

                def check(reaction, user):
                    return user != pic.author and (str(reaction) == next or str(reaction) == stop or str(reaction) == back)

                try:
                    reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
                except asyncio.TimeoutError:
                    going = False

                if str(reaction) == next:
                    await pic.delete()
                    if index != len(Cute_Necks) - 1:
                        index = index + 1
                    else:
                        await ctx.send("That's the end")
                        index = index
                elif str(reaction) == back:
                    await pic.delete()
                    index = index - 1
                elif str(reaction) == stop:
                    await pic.delete()
                    going = False

    elif item == "ring":
        if style == "fancy":
            going = True
            index = 0
            while going:
                Fancy_Rs = os.listdir(path="Fancy_Rings")
                pic = await ctx.send(file=discord.File("Fancy_Rings/" + Fancy_Rs[index]), delete_after=120.0)
                await pic.add_reaction(back)
                await pic.add_reaction(stop)
                await pic.add_reaction(next)

                def check(reaction, user):
                    return user != pic.author and (str(reaction) == next or str(reaction) == stop or str(reaction) == back)

                try:
                    reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
                except asyncio.TimeoutError:
                    going = False

                if str(reaction) == next:
                    await pic.delete()
                    if index != len(Fancy_Rs) - 1:
                        index = index + 1
                    else:
                        await ctx.send("That's the end")
                        index = index
                elif str(reaction) == back:
                    await pic.delete()
                    index = index - 1
                elif str(reaction) == stop:
                    await pic.delete()
                    going = False

        elif style == "casual":
            going = True
            index = 0
            while going:
                Casual_Rs = os.listdir(path="Casual_Rings")
                pic = await ctx.send(file=discord.File("Casual_Rings/" + Casual_Rs[index]), delete_after=120.0)
                await pic.add_reaction(back)
                await pic.add_reaction(stop)
                await pic.add_reaction(next)

                def check(reaction, user):
                    return user != pic.author and (str(reaction) == next or str(reaction) == stop or str(reaction) == back)

                try:
                    reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
                except asyncio.TimeoutError:
                    going = False

                if str(reaction) == next:
                    await pic.delete()
                    if index != len(Casual_Rs) - 1:
                        index = index + 1
                    else:
                        await ctx.send("That's the end")
                        index = index
                elif str(reaction) == back:
                    await pic.delete()
                    index = index - 1
                elif str(reaction) == stop:
                    await pic.delete()
                    going = False

        elif style == "cute":
            going = True
            index = 0
            while going:
                Cute_Rs = os.listdir(path="Cute_Rings")
                pic = await ctx.send(file=discord.File("Cute_Rings/" + Cute_Rs[index]), delete_after=120.0)
                await pic.add_reaction(back)
                await pic.add_reaction(stop)
                await pic.add_reaction(next)

                def check(reaction, user):
                    return user != pic.author and (str(reaction) == next or str(reaction) == stop or str(reaction) == back)

                try:
                    reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
                except asyncio.TimeoutError:
                    going = False

                if str(reaction) == next:
                    await pic.delete()
                    if index != len(Cute_Rs) - 1:
                        index = index + 1
                    else:
                        await ctx.send("That's the end")
                        index = index
                elif str(reaction) == back:
                    await pic.delete()
                    index = index - 1
                elif str(reaction) == stop:
                    await pic.delete()
                    going = False

    elif item == "hat":
        if style == "fancy":
            going = True
            index = 0
            while going:
                Fancy_Hts = os.listdir(path="Fancy_Hats")
                pic = await ctx.send(file=discord.File("Fancy_Hats/" + Fancy_Hts[index]), delete_after=120.0)
                await pic.add_reaction(back)
                await pic.add_reaction(stop)
                await pic.add_reaction(next)

                def check(reaction, user):
                    return user != pic.author and (str(reaction) == next or str(reaction) == stop or str(reaction) == back)

                try:
                    reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
                except asyncio.TimeoutError:
                    going = False

                if str(reaction) == next:
                    await pic.delete()
                    if index != len(Fancy_Hts) - 1:
                        index = index + 1
                    else:
                        await ctx.send("That's the end")
                        index = index
                elif str(reaction) == back:
                    await pic.delete()
                    index = index - 1
                elif str(reaction) == stop:
                    await pic.delete()
                    going = False

        elif style == "casual":
            going = True
            index = 0
            while going:
                Casual_Hts = os.listdir(path="Casual_Hats")
                pic = await ctx.send(file=discord.File("Casual_Hats/" + Casual_Hts[index]), delete_after=120.0)
                await pic.add_reaction(back)
                await pic.add_reaction(stop)
                await pic.add_reaction(next)

                def check(reaction, user):
                    return user != pic.author and (str(reaction) == next or str(reaction) == stop or str(reaction) == back)

                try:
                    reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
                except asyncio.TimeoutError:
                    going = False

                if str(reaction) == next:
                    await pic.delete()
                    if index != len(Casual_Hts) - 1:
                        index = index + 1
                    else:
                        await ctx.send("That's the end")
                        index = index
                elif str(reaction) == back:
                    await pic.delete()
                    index = index - 1
                elif str(reaction) == stop:
                    await pic.delete()
                    going = False

        elif style == "cute":
            going = True
            index = 0
            while going:
                Cute_Hts = os.listdir(path="Cute_Hats")
                pic = await ctx.send(file=discord.File("Cute_Hats/" + Cute_Hts[index]), delete_after=120.0)
                await pic.add_reaction(back)
                await pic.add_reaction(stop)
                await pic.add_reaction(next)

                def check(reaction, user):
                    return user != pic.author and (str(reaction) == next or str(reaction) == stop or str(reaction) == back)

                try:
                    reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
                except asyncio.TimeoutError:
                    going = False

                if str(reaction) == next:
                    await pic.delete()
                    if index != len(Cute_Hts) - 1:
                        index = index + 1
                    else:
                        await ctx.send("That's the end")
                        index = index
                elif str(reaction) == back:
                    await pic.delete()
                    index = index - 1
                elif str(reaction) == stop:
                    await pic.delete()
                    going = False


async def shoes(ctx, cli, style):
    await ctx.send("You chose " + style)
    next = "\u27A1"
    back = "\u2B05"
    stop = "\U0001F6D1"
    if style == "fancy":
        Fancy_Shs = os.listdir(path="Fancy_Shoes")
        index = 0
        going = True
        while going:
            pic = await ctx.send(file=discord.File("Fancy_Shoes/" + Fancy_Shs[index]), delete_after=120.0)
            await pic.add_reaction(back)
            await pic.add_reaction(stop)
            await pic.add_reaction(next)

            def check(reaction, user):
                return user != pic.author and (str(reaction) == back or str(reaction) == stop or str(reaction) == next)

            try:
                reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                going = False

            if str(reaction) == next:
                await pic.delete()
                if index != len(Fancy_Shs) - 1:
                    index = index + 1
                else:
                    await ctx.send("That's the end")
                    index = index
            elif str(reaction) == back:
                await pic.delete()
                index -= 1
            elif str(reaction) == stop:
                await pic.delete()
                going = False
    elif style == "casual":
        Casual_Shs = os.listdir(path="Casual_Shoes")
        index = 0
        going = True
        while going:
            pic = await ctx.send(file=discord.File("Casual_Shoes/" + Casual_Shs[index]), delete_after=120.0)
            await pic.add_reaction(back)
            await pic.add_reaction(stop)
            await pic.add_reaction(next)

            def check(reaction, user):
                return user != pic.author and (str(reaction) == back or str(reaction) == stop or str(reaction) == next)
            try:
                reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                going = False

            if str(reaction) == next:
                await pic.delete()
                if index != len(Casual_Shs) - 1:
                    index = index + 1
                else:
                    await ctx.send("That's the end")
                    index = index
            elif str(reaction) == back:
                await pic.delete()
                index -= 1
            elif str(reaction) == stop:
                await pic.delete()
                going = False
    elif style == "sporty":
        Sporty_Shs = os.listdir(path="Sporty_Shoes")
        index = 0
        going = True
        while going:
            pic = await ctx.send(file=discord.File("Sporty_Shoes/" + Sporty_Shs[index]), delete_after=120.0)
            await pic.add_reaction(back)
            await pic.add_reaction(stop)
            await pic.add_reaction(next)

            def check(reaction, user):
                return user != pic.author and (str(reaction) == back or str(reaction) == stop or str(reaction) == next)

            try:
                reaction, user = await cli.wait_for('reaction_add', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                going = False

            if str(reaction) == next:
                await pic.delete()
                if index != len(Sporty_Shs) - 1:
                    index = index + 1
                else:
                    await ctx.send("That's the end")
                    index = index
            elif str(reaction) == back:
                await pic.delete()
                index -= 1
            elif str(reaction) == stop:
                await pic.delete()
                going = False