import discord
from discord.ext import commands
import time

token2 = "OTg0MTI4MTI4NTA5MTYxNTIz.Giekm3.O-mxxkHHL2Jza5qrg7TjyeJnohepsEUfoPOhUM"
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!!", intents=intents)


client.remove_command('help')


@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, time, reason=None):
    desctime = time
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    time_convert = {"s":1, "m":60, "h":3600, "d":86400, "w":604800, "mo":18144000, "y":31536000}
    tempmute= int(time[:-1]) * time_convert[time[-1]]
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted   for {desctime} ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=True)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await asyncio.sleep(tempmute)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")
    await member.remove_roles(mutedRole)


client.run(token2)
