from discord.ext import commands
from discord import channel, utils
import discord
import asyncio
import random
from discord.ext.commands import bot

import discord
from discord.ext import commands
class welcome(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
          
        if member.guild.id==799526257506254868:
      
            x='''> <a:capoopoof:847413169995513916>  <#800095824310566922>  <#800116012954550292> <#800116101580193832>'''
            
            em=discord.Embed(title="You made it!",description=x,color=0x2f3136)
            em.set_author(name='Cloudy With A Chance of Depression',icon_url="https://i.imgur.com/QQcLvbH.gif")
            
            guild=self.bot.get_guild(799526257506254868)
            channel = guild.get_channel(827008183692296222) 
            y=['<a:hiwave:845251975281115146>','<:potatospired:842744736439074877>','<:Ooyes:845223747060367370>','<:FlushProud:843845968037937153>','<:hehe:827599471156133958>','<:potatocute:847412181364506644>','<a:capooeyes:847413043160023060>','<a:capoopat:847412985705922621>','<a:capoopoof:847413169995513916>']
            m=await channel.send(f'<a:animesip:823846730888904724> {member.mention} <@&802797577300213790>',embed=em)
            await m.add_reaction(f'{random.choice(y)}')
    @commands.command()
    async def testjoin(self,message):
        
        if message.author.id in [261742964441612298,533696842613915658]:
             x='''> <a:capoopoof:847413169995513916>   <#800095824310566922>  <#800116012954550292> <#800116101580193832>'''
             e=discord.Embed(title="You made it!",description=x,color=0x2f3136)
             e.set_author(name='Cloudy With A Chance of Depression',icon_url="https://i.imgur.com/QQcLvbH.gif")
             
             guild=self.bot.get_guild(799526257506254868)
             channel = guild.get_channel(827008183692296222) 
             y=['<a:hiwave:845251975281115146>','<:potatospired:842744736439074877>','<:Ooyes:845223747060367370>','<:FlushProud:843845968037937153>','<:hehe:827599471156133958>','<:potatocute:847412181364506644>','<a:capooeyes:847413043160023060>','<a:capoopat:847412985705922621>','<a:capoopoof:847413169995513916>']
             await m.add_reaction(f'{random.choice(y)}')
def setup(bot):
    bot.add_cog(welcome(bot))
