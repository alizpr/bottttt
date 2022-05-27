import discord
from discord.ext import commands
import time

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="-", intents=intents)


@bot.event
async def on_ready():
    print('Online shode')


@bot.command()
async def dm(ctx, *, msg=None):
    sendedmsg = []
    members = ctx.guild.members
    if msg != None:
        for member in members:
            mesg = member.mention + "\n\n\n\n" + msg
            try:
                await member.send(mesg)
                print(f"Sended Message | {member.name}")
                await ctx.send(member.mention + "|" + member.name + "|" + member.id)
                sendedmsg.append(member.mention)
            except:
                print(f"Cloudnt Send Message To | {member.name}")
            time.sleep(16)

        embed = discord.Embed(
                title='list of members',
                colour=discord.Colour.purple()
                )
        embed.add_field(name=f"total = {length(sendedmsg)}",value= sendedmsg,inline=False)
        await ctx.channel.send(embed=embed)

    else:
        await ctx.send("ye msg bego man beheshon migam")


bot.run('OTc5MzM4NDU0NjQ5NDM0MTQy.Gm9M9d.MEmNSHf0PVc-lw1HxwK5apU9qtir-8_x8f6DTs')