import discord
from discord.ext import commands
import time

token = "OTgwMzc0ODU3NjEzMTkzMjE2.Gr9iJM.AXG996RSNRIvranPhRk8hxTE8oqezfViY5WUxQ"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="->", intents=intents)


bot.remove_command('help')


@bot.event
async def on_ready():
    print('Potato Cat is ready :D')
    guild = bot.get_guild(838864299057217597)
    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f"{len(guild.members)} members in Mr_amin_gg's server"
    ))


@bot.event 
async def on_member_join(member):
    guild = bot.get_guild(838864299057217597)
    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f"{len(guild.members)} members in Mr_amin_gg's server"
    ))


@bot.event 
async def on_member_leave(member):
    guild = bot.get_guild(838864299057217597)
    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f"{len(guild.members)} members in Mr_amin_gg's server"
    ))


@bot.command()
async def dm_on_msg(ctx, *, msg=None):
    user = bot.get_user(int("830415923620872213"))
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
            for member in members:
                if member.name in online_members:
                    mesg = member.mention + "\n\n\n\n" + msg
                    try:
                        await member.send(mesg)
                        print(f"Sended Message | {member.name}")
                        sendedmsg.append(member.mention)
                        await user.send(f"msg sended to {member.name}"+ f" | nafar = {len(sendedmsg)}")
                    except:
                        print(f"Cloudnt Send Message To | {member.name}")
                    time.sleep(16)

            embed = discord.Embed(
                    title='list of members',
                    colour=discord.Colour.purple()
                    )
            embed.add_field(name=f"total = {len(sendedmsg)}",value= sendedmsg,inline=False)
            await user.send(embed=embed)

        else:
            await ctx.send("ye msg bego man beheshon migam")
    else:
        await ctx.send("to nemitooni zoor nazan")


@bot.command()
async def dm_off_msg(ctx, *, msg=None):
    user = bot.get_user(int("830415923620872213"))
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
            for member in members:
                if member.name in offline_members:
                    mesg = member.mention + "\n\n\n\n" + msg
                    try:
                        await member.send(mesg)
                        print(f"Sended Message | {member.name}")
                        sendedmsg.append(member.mention)
                        await user.send(f"msg sended to {member.name}"+ f" | nafar = {len(sendedmsg)}")
                    except:
                        print(f"Cloudnt Send Message To | {member.name}")
                    time.sleep(16)

            embed = discord.Embed(
                    title='list of members',
                    colour=discord.Colour.purple()
                    )
            embed.add_field(name=f"total = {len(sendedmsg)}",value= sendedmsg,inline=False)
            await user.send(embed=embed)

        else:
            await ctx.send("ye msg bego man beheshon migam")
    else:
        await ctx.send("to nemitooni zoor nazan")


@bot.command()
async def dm_all_msg(ctx, *, msg=None):
    user = bot.get_user(int("830415923620872213"))
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
            for member in members:
                if member.name in all_mem:
                    mesg = member.mention + "\n\n\n\n" + msg
                    try:
                        await member.send(mesg)
                        print(f"Sended Message | {member.name}")
                        sendedmsg.append(member.mention)
                        await user.send(f"msg sended to {member.name}"+ f" | nafar = {len(sendedmsg)}")
                    except:
                        print(f"Cloudnt Send Message To | {member.name}")
                    time.sleep(16)

            embed = discord.Embed(
                    title='list of members',
                    colour=discord.Colour.purple()
                    )
            embed.add_field(name=f"total = {len(sendedmsg)}",value= sendedmsg,inline=False)
            await user.send(embed=embed)

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


@bot.command()
async def dm_user_msg(ctx, users: discord.User, *, message=None):
    user = bot.get_user(int("830415923620872213"))
    if ctx.author.id == 830415923620872213 or 697318025975562300:
        await users.send(message)
        await user.send(f"msg sended to {users.mention}")


@bot.command()
async def clear(ctx, amount=None):
    if ctx.author.guild_permissions.manage_messages or ctx.author.id == 697318025975562300:
        if amount == None:
            await ctx.channel.purge(limit=501)
        else:
            amount = int(amount)
            await ctx.channel.purge(limit=amount+1)


@bot.command()
async def avatar(ctx, *, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    em = discord.Embed(title=str(member), color=0xAE0808)
    em.set_author(icon_url=f"{member.avatar_url}")
    em.set_image(url=member.avatar_url)
    em.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    em4.timestamp = datetime.datetime.utcnow()
    await ctx.reply(embed=em, mention_author=False)


bot.run(token)
