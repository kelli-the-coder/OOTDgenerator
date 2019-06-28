import discord
from discord.ext import commands
import asyncio
import time
import Outfit_Pictures
#Season function definitions:
async def SpringOrSummer(ctx, gender, cli):
    channel = ctx.channel
    season = "SpringOrSummer"
    await ctx.send("You chose Spring/Summer!")
    if gender == "girl":
        await ctx.send("What style would you like? \nPretty, Sporty, Casual, Fancy ")
        def check(m):
            return m.channel == channel and (m.content.lower() == "pretty" or m.content.lower() == "sporty" or m.content.lower() == "casual" or m.content.lower() == "fancy")
        style = await cli.wait_for("message", check=check, timeout=60.0)

        if style.content.lower() == "pretty":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-SpringOrSummer-Pretty.jpg"))
        elif style.content.lower() == "sporty":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-SpringOrSummer-Sporty.jpg"))
        elif style.content.lower() == "casual":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-SpringOrSummer-Casual.jpg"))
        elif style.content.lower() == "fancy":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-SpringOrSummer-Fancy.jpg"))

    if gender == "boy":
        await ctx.send("What style would you like? \nSporty, Casual, Fancy, Nerdy")
        def check(m):
            return m.channel == channel and (m.content.lower() == "sporty" or m.content.lower() == "casual" or m.content.lower() == "casual" or m.content.lower() == "fancy" or m.content.lower() == "nerdy")
        style = await cli.wait_for("message", check=check, timeout=60.0)

        if style.content.lower() == "sporty":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-SpringOrSummer-Sporty.jpg"))
        elif style.content.lower() == "casual":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-SpringOrSummer-Casual.jpg"))
        elif style.content.lower() == "fancy":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-SpringOrSummer-Fancy.jpg"))
        elif style.content.lower() == "nerdy":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-SpringOrSummer-Nerdy.jpg"))

    if gender == "neutral":
        await ctx.send("What style would you like? \nCasual, Professional, Flex, Rapper, Western")
        def check(m):
            return m.channel == channel and (m.content.lower() == "casual" or m.content.lower() == "professional" or m.content.lower() == "flex" or m.content.lower() == "rapper" or m.content.lower() == "western")
        style = await cli.wait_for("message", check=check, timeout=60.0)

        if style.content.lower() == "casual":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-SpringOrSummer-Casual.jpg"))
        elif style.content.lower() == "professional":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-SpringOrSummer-Professional.jpg"))
        elif style.content.lower() == "flex":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-SpringOrSummer-Flex.jpg"))
        elif style.content.lower() == "rapper":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-SpringOrSummer-Rapper.jpg"))
        elif style.content.lower() == "western":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-SpringOrSummer-Western.jpg"))


async def winter(ctx, gender, cli):
    channel = ctx.channel
    season = "winter"
    await ctx.send("You chose Winter!")
    if gender == "girl":
        await ctx.send("What style would you like? \nCute, Sporty, Casual, Fancy ")
        def check(m):
            return m.channel == channel and (m.content.lower() == "cute" or m.content.lower() == "sporty" or m.content.lower() == "casual" or m.content.lower() == "fancy")

        style = await cli.wait_for("message", check=check, timeout=60.0)

        if style.content.lower() == "cute":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-Winter-Cute.jpg"))
        elif style.content.lower() == "sporty":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-Winter-Sporty.jpg"))
        elif style.content.lower() == "casual":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-Winter-Casual.jpg"))
        elif style.content.lower() == "fancy":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-Winter-Fancy.jpg"))

    elif gender == "boy":
        await ctx.send("What style would you like? \nSporty, Casual, Fancy, Nerdy")
        def check(m):
            return m.channel == channel and (m.content.lower() == "sporty" or m.content.lower() == "casual" or m.content.lower() == "casual" or m.content.lower() == "fancy" or m.content.lower() == "nerdy")
        style = await cli.wait_for("message", check=check, timeout=60.0)

        if style.content.lower() == "sporty":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-Winter-Sporty.jpg"))
        elif style.content.lower() == "casual":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-Winter-Casual.jpg"))
        elif style.content.lower() == "fancy":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-Winter-Fancy.jpg"))
        elif style.content.lower() == "nerdy":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-Winter-Nerdy.jpg"))

    elif gender == "neutral":
        await ctx.send("What style would you like? \nCasual, Professional, Flex, Rapper, Western")
        def check(m):
            return m.channel == channel and (m.content.lower() == "casual" or m.content.lower() == "professional" or m.content.lower() == "flex" or m.content.lower() == "rapper" or m.content.lower() == "western")
        style = await cli.wait_for("message", check=check, timeout=60.0)

        if style.content.lower() == "casual":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-Winter-Casual.jpg"))
        elif style.content.lower() == "professional":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-Winter-Professional.jpg"))
        elif style.content.lower() == "flex":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-Winter-Flex.png"))
        elif style.content.lower() == "rapper":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-Winter-Rapper.jpg"))
        elif style.content.lower() == "western":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-Winter-Western.jpg"))

async def autumn(ctx, gender, cli):
    season = "autumn"
    channel = ctx.channel
    await ctx.send("You chose Autumn!")
    if gender == "girl":
        await ctx.send("What style would you like? \nCute, Sporty, Casual, Fancy ")
        def check(m):
            return m.channel == channel and (m.content.lower() == "cute" or m.content.lower() == "sporty" or m.content.lower() == "casual" or m.content.lower() == "fancy")

        style = await cli.wait_for("message", check=check, timeout=60.0)

        if style.content.lower() == "cute":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-Autumn-Cute.jpg"))
        elif style.content.lower() == "sporty":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-Autumn-Sporty.jpg"))
        elif style.content.lower() == "casual":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-Autumn-Casual.jpg"))
        elif style.content.lower() == "fancy":
            await ctx.send(file=discord.File("Outfit_Pictures/Girl-Autumn-Fancy.jpg"))

    elif gender == "boy":
        await ctx.send("What style would you like? \nSporty, Casual, Fancy, Nerdy")
        def check(m):
            return m.channel == channel and (m.content.lower() == "sporty" or m.content.lower() == "casual" or m.content.lower() == "casual" or m.content.lower() == "fancy" or m.content.lower() == "nerdy")
        style = await cli.wait_for("message", check=check, timeout=60.0)

        if style.content.lower() == "sporty":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-Autumn-Sporty.jpg"))
        elif style.content.lower() == "casual":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-Autumn-Casual.jpg"))
        elif style.content.lower() == "fancy":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-Autumn-Fancy.jpg"))
        elif style.content.lower() == "nerdy":
            await ctx.send(file=discord.File("Outfit_Pictures/Boy-Autumn-Nerdy.jpg"))

    elif gender == "neutral":
        await ctx.send("What style would you like? \nCasual, Professional, Flex, Rapper, Western")
        def check(m):
            return m.channel == channel and (m.content.lower() == "casual" or m.content.lower() == "professional" or m.content.lower() == "flex" or m.content.lower() == "rapper" or m.content.lower() == "western")
        style = await cli.wait_for("message", check=check, timeout=60.0)

        if style.content.lower() == "casual":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-Autumn-Casual.jpg"))
        elif style.content.lower() == "professional":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-Autumn-Professional.jpg"))
        elif style.content.lower() == "flex":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-Autumn-Flex.jpg"))
        elif style.content.lower() == "rapper":
            await ctx.send(file=discord.File("Outfit_Pictures/Neutral-Autumn-Rapper.jpg"))
        elif style.content.lower() == "western":
            await ctx.send(file=discord.File("Neutral-Autumn-Western.jpg"))