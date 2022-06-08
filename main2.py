import discord
from discord.ext import commands
import time
import asyncio

token2 = "OTg0MTI4MTI4NTA5MTYxNTIz.Giekm3.O-mxxkHHL2Jza5qrg7TjyeJnohepsEUfoPOhUM"
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!!", intents=intents)


client.remove_command('help')


@client.event
async def on_ready():
    print("hello")


@client.command()
async def mute(ctx, member : discord.Member, time=0, d=None, *,reason=None):
    if not member or time == 0 or time == str:
        await ctx.channel.send(embed=commanderror)
        return
    elif reason == None:
        reason = "No Reason Provided"

    muteRole = discord.utils.get(ctx.guild.roles, id=984145664659308604)
    await member.add_roles(muteRole)

    tempMuteEmbed = discord.Embed(description=f"**Reason:** {reason}",colour=discord.Colour.purple())
    tempMuteEmbed.set_author(name=f"{member} Has Been Muted", icon_url=f"{member.avatar_url}")

    await ctx.channel.send(embed=tempMuteEmbed)

    tempMuteModLogEmbed = discord.Embed(colour=discord.Colour.purple())
    tempMuteModLogEmbed.set_author(name=f"`MUTE` {member}", icon_url=f"{member.avatar_url}")
    tempMuteModLogEmbed.add_field(name="User:", value=f"{member.mention}")
    tempMuteModLogEmbed.add_field(name="Moderator:", value=f"{ctx.message.author.mention}")
    tempMuteModLogEmbed.add_field(name="Reason:", value=f"{reason}", inline=False)
    tempMuteModLogEmbed.add_field(name="Duration:", value=f"{str(time)}{d}")
    modlog = client.get_channel(983657238428262424)
    await modlog.send(embed=tempMuteModLogEmbed)

    tempMuteDM = discord.Embed(colour=discord.Colour.purple(), title="`Mute Notification`", description="You Were Muted In **Mr_amin_gg**'s server")
    tempMuteDM.add_field(name="Reason:", value=f"{reason}")
    tempMuteDM.add_field(name="Duration:", value=f"{time}{d}")

    userToDM = client.get_user(member.id)
    await userToDM.send(embed=tempMuteDM)

    if d == "s":
        await asyncio.sleep(time)

    if d == "m":
        await asyncio.sleep(time*60)

    if d == "h":
        await asyncio.sleep(time*60*60)

    if d == "d":
        await asyncio.sleep(time*60*60*24)

    await member.remove_roles(muteRole)

    unMuteModLogEmbed = discord.Embed(colour=discord.Colour.purple())
    unMuteModLogEmbed.set_author(name=f"`UNMUTE` {member}", icon_url=f"{member.avatar_url}")
    unMuteModLogEmbed.add_field(name="User:", value=f"{member.mention}")
    modlog = client.get_channel(983657238428262424)
    await modlog.send(embed=unMuteModLogEmbed)


client.run(token2)
