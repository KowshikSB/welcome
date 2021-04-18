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
          
  
      
          x='''<a:kawaiiStarryCloud:824531125678243891> <#800095824310566922> 
<a:kawaiiStarryCloud:824531125678243891> <#800116012954550292>
<a:kawaiiStarryCloud:824531125678243891> <#827008183692296222>'''
          
          em=discord.Embed(title="Cloudy With A Chance of Depression",description=x,color=0x2f3136)
          em.set_author(name=f'{member.name}#{member.discriminator}',icon_url=member.avatar_url)
          em.set_thumbnail(url="https://cdn.discordapp.com/attachments/799598027257937921/829726047883886622/tenor_3.gif") 
          guild=self.bot.get_guild(799526257506254868)
          channel = guild.get_channel(827008183692296222) 
          
          await channel.send(f'<a:animesip:823846730888904724> {member.mention} <@&802797577300213790>',embed=em)
def setup(bot):
    bot.add_cog(welcome(bot))
