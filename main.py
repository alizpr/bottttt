import discord
from discord.ext import commands
import time

token = "OTgwMzc0ODU3NjEzMTkzMjE2.Gr9iJM.AXG996RSNRIvranPhRk8hxTE8oqezfViY5WUxQ"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="->", intents=intents)


bot.remove_command('help')


@bot.event
async def on_ready():
    print('Online shode')


@bot.command()
async def dm_on_msg(ctx, *, msg=None):
    if ctx.author.id == 830415923620872213:
        sendedmsg = []
        online_members = []
        offline_members = []
        for member in ctx.guild.members:
            if member.status is not discord.Status.offline:
                online_members.append(member.name)
            else:
                offline_members.append(member.name)

        members = ctx.guild.members
        if msg != None:
            if members.name in online_members:
                for member in members:
                    mesg = member.mention + "\n\n\n\n" + msg
                    try:
                        await member.send(mesg)
                        print(f"Sended Message | {member.name}")
                        sendedmsg.append(member.mention)
                        await ctx.channel.send(("Sended to  " + member.mention) + f" | nafar = {len(sendedmsg)}")
                    except:
                        print(f"Cloudnt Send Message To | {member.name}")
                    time.sleep(16)

                embed = discord.Embed(
                        title='list of members',
                        colour=discord.Colour.purple()
                        )
                embed.add_field(name=f"total = {len(sendedmsg)}",value= sendedmsg,inline=False)
                await ctx.channel.send(embed=embed)

            else:
                await ctx.send("ye msg bego man beheshon migam")
    else:
        await ctx.send("to nemitooni zoor nazan")


@bot.command()
async def dm_off_msg(ctx, *, msg=None):
    if ctx.author.id == 830415923620872213:
        sendedmsg = []
        online_members = []
        offline_members = []
        for member in ctx.guild.members:
            if member.status is not discord.Status.offline:
                online_members.append(member.name)
            else:
                offline_members.append(member.name)

        members = ctx.guild.members
        if msg != None:
            if members.name in offline_members:
                for member in members:
                    mesg = member.mention + "\n\n\n\n" + msg
                    try:
                        await member.send(mesg)
                        print(f"Sended Message | {member.name}")
                        sendedmsg.append(member.mention)
                        await ctx.channel.send(("Sended to  " + member.mention) + f" | nafar = {len(sendedmsg)}")
                    except:
                        print(f"Cloudnt Send Message To | {member.name}")
                    time.sleep(16)

                embed = discord.Embed(
                        title='list of members',
                        colour=discord.Colour.purple()
                        )
                embed.add_field(name=f"total = {len(sendedmsg)}",value= sendedmsg,inline=False)
                await ctx.channel.send(embed=embed)

            else:
                await ctx.send("ye msg bego man beheshon migam")
    else:
        await ctx.send("to nemitooni zoor nazan")


@bot.command()
async def dm_all_msg(ctx, *, msg=None):
    if ctx.author.id == 830415923620872213:
        sendedmsg = []
        all_mem = []
        for member in ctx.guild.members:
            if member.status is not discord.Status.offline:
                all_mem.append(member.name)
            else:
                all_mem.append(member.name)

        members = ctx.guild.members
        if msg != None:
            if members.name in all_mem:
                for member in members:
                    mesg = member.mention + "\n\n\n\n" + msg
                    try:
                        await member.send(mesg)
                        print(f"Sended Message | {member.name}")
                        sendedmsg.append(member.mention)
                        await ctx.channel.send(("Sended to  " + member.mention) + f" | nafar = {len(sendedmsg)}")
                    except:
                        print(f"Cloudnt Send Message To | {member.name}")
                    time.sleep(16)

                embed = discord.Embed(
                        title='list of members',
                        colour=discord.Colour.purple()
                        )
                embed.add_field(name=f"total = {len(sendedmsg)}",value= sendedmsg,inline=False)
                await ctx.channel.send(embed=embed)

            else:
                await ctx.send("ye msg bego man beheshon migam")
    else:
        await ctx.send("to nemitooni zoor nazan")


@bot.command()
async def join(ctx):
    if ctx.author.id == 830415923620872213:
        channel = ctx.author.voice.channel
        await channel.connect()
@bot.command()
async def leave(ctx):
    if ctx.author.id == 830415923620872213:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("to nemitooni zoor nazan")

bot.run(token)
