#Import Discord Package
import discord

from typing import ContextManager
import json
from discord import message
from discord import colour
from discord import embeds
from discord.embeds import Embed

from discord.utils import _MARKDOWN_ESCAPE_COMMON
import requests
import random
from discord.ext import commands
from datetime import datetime
 




# Client (our bot)
client = discord.Client()



    
#commands
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event 
async def on_ready():
   print("MORDEX IS HERE")

@client.event
async def on_message(message):
  

      
   if message.content.startswith ('$ver'):
      
      await message.channel.send('```Version 1.0```')

   if message.content.startswith ('$games'):
      
       await message.channel.send(
       """```PC Games - CSGO,Valorant,Call of Duty MW,etc
      Mobile Games - PUBG,FreeFire,Among US,etc
         
       ```""")

   if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

   if message.content.startswith ('$creator'):
      await message.channel.send ('```Created by Creator - Himunoid/Himanshu Aundhe``` ')

   if message.content.startswith('$help'):
        
         
        embed=discord.Embed(title="Help", description="Commands for MORDEX", color=0x00c0f0, timestamp=datetime.utcnow())
        embed.set_author(name="MORDEX", icon_url="https://cdn.discordapp.com/avatars/858237991357120563/a5820d89d6dfab7b0757965dcffbbdcb.png?size=128")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/750851849019719741/a_831cad9b1be2135e19c9493c0d1b3e01.gif?size=128")
        embed.add_field(name="$help", value="For using all the commands", inline=False)
        embed.add_field(name="$ver", value="For showing the Version of Bot", inline=False)
        embed.add_field(name="$inspire", value="For a Motivational quote", inline=False)
        embed.add_field(name="$games", value="List of Popular Games", inline=False)
        embed.add_field(name="$creator", value="Info about Creator", inline=False)
        embed.set_footer(text="© Copyright and Legal")
        await message.channel.send(embed=embed)





         
          
















   



#run the client on the server
client.run('ODU4MjM3OTkxMzU3MTIwNTYz.YNbOag.tz4lW43FLe-y0WwUM3RQJ4jH8Kg')

