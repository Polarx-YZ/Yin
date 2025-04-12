import discord
from discord.ext import commands
import pokebase as pb


class Pokemon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
    # @SpaceDuck16 
    '''
    Docs: https://github.com/PokeAPI/pokebase
    
    How to implement command:
    - get input of which pokemon is being searched  
        
    - get all required data from the pokemon
        pb.pokemon() # Returns a pokemon's data
        set variables
    
    - put all the data into a nice embed
        discord.Embed() # Creates an embed
    
    - send the embed to the user
        ctx.reply(embed=embed_variable)
    
    When done set hidden to False
    '''
    
    @commands.command(hidden=True)
    async def pokemon(self, ctx, pokemon: str):
        pass
    

    
async def setup(bot):
    await bot.add_cog(Pokemon(bot))