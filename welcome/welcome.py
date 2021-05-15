from discord.ext import commands
from discord import channel, utils
import discord
import asyncio

from discord.ext.commands import bot

import discord
from discord.ext import commands
class welcome(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
          
        if member.guild.id==799526257506254868:
      
            x='''<a:kawaiiStarryCloud:824531125678243891> <#800095824310566922> 
<a:kawaiiStarryCloud:824531125678243891> <#800116012954550292>
<a:kawaiiStarryCloud:824531125678243891> <#827008183692296222>'''
            
            em=discord.Embed(title="Cloudy With A Chance of Depression",description=x,color=0x2f3136)
            em.set_author(name=f'{member.name}#{member.discriminator}',icon_url=member.avatar_url)
            em.set_thumbnail(url="https://i.imgur.com/y4tOjWS.gif") 
            guild=self.bot.get_guild(799526257506254868)
            channel = guild.get_channel(827008183692296222) 
            
            await channel.send(f'<a:animesip:823846730888904724> {member.mention} <@&802797577300213790>',embed=em)
    @commands.command()
    async def testjoin(self,message):
        if message.author.id in [261742964441612298,533696842613915658]:
             x='''<a:kawaiiStarryCloud:824531125678243891> <#800095824310566922> 
<a:kawaiiStarryCloud:824531125678243891> <#800116012954550292>
<a:kawaiiStarryCloud:824531125678243891> <#827008183692296222>'''
          
             e=discord.Embed(title="Cloudy With A Chance of Depression",description=x,color=0x2f3136)
             e.set_author(name=f'{message.author.name}#{message.author.discriminator}',icon_url=message.author.avatar_url)
             e.set_thumbnail(url="https://i.imgur.com/y4tOjWS.gif") 
             guild=self.bot.get_guild(799526257506254868)
             channel = guild.get_channel(827008183692296222) 
             await channel.send(f'<a:animesip:823846730888904724> {message.author.mention} <@&802797577300213790>',embed=e)
        
def setup(bot):
    bot.add_cog(welcome(bot))
