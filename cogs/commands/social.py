import discord
from discord.ext import commands

from easy_pil import Editor, load_image_async

class Social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def slap(self, ctx, victim: discord.Member):
        editor = Editor("images/slap.jpg")
        
        pfp_owner = ctx.author.avatar.url
        victim_pfp_owner = victim.avatar.url

        if ctx.author.id == victim.id:
            pfp_owner = self.bot.user.avatar.url
        
        pfp = await load_image_async(pfp_owner) 
        pfp2 = await load_image_async(victim_pfp_owner)
        
        # Place the invoker's pfp
        pfp = pfp.resize((150, 150))
        pfp = pfp.rotate(15, expand=True)
        editor.paste(pfp, (-15, 65))
        
        # Place the victim's pfp
        pfp2 = pfp2.resize((220, 220))
        pfp2 = pfp2.rotate(-35, expand=True)
        editor.paste(pfp2, (350, 10))

        embed = discord.Embed(
            description = f"### {ctx.author.mention} slapped {victim.mention}!!",
            color = discord.Color.red()
        )
        
        file = discord.File(fp=editor.image_bytes, filename="file.png")
        
        embed.set_image(url="attachment://file.png")
        await ctx.reply(file=file, embed=embed)
    
async def setup(bot):
    await bot.add_cog(Social(bot))