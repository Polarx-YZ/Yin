import discord
from discord.ext import commands

import PIL.Image as Image
from io import BytesIO
import requests

class ImageGeneration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def slap(self, ctx, victim: discord.Member):
        slap_template = Image.open("images/slap.jpg")
        
        pfp = await self.open_pfp(ctx.author.avatar.url) 
        pfp2 = await self.open_pfp(victim.avatar.url)
        
        #slap_template = slap_template.resize((405 * 2, 612 * 2))
        
        pfp = pfp.resize((150, 150))
        mask = Image.new('L', pfp.size, 255)
        pfp = pfp.rotate(15, expand=True)
        mask = mask.rotate(15, expand=True)
        slap_template.paste(pfp, (-15, 65), mask)
        
        pfp2 = pfp2.resize((220, 220))
        mask = Image.new('L', pfp2.size, 255)
        pfp2 = pfp2.rotate(-35, expand=1)
        mask = mask.rotate(-35, expand=True)
        slap_template.paste(pfp2, (350, 10), mask)
        
        embed = discord.Embed(
            description = f"### {ctx.author.mention} slapped {victim.mention}!!",
            color = discord.Color.red()
        )
        
        
        with BytesIO() as image_binary:
            slap_template.save(image_binary, "PNG")
            image_binary.seek(0)
            file = discord.File(fp=image_binary, filename="file.png")
            
            embed.set_image(url="attachment://file.png")
            await ctx.send(file=file, embed=embed)
    
    async def open_pfp(self, asset):
        data = BytesIO(requests.get(asset).content)
        pfp = Image.open(data)
        return pfp
    
async def setup(bot):
    await bot.add_cog(ImageGeneration(bot))