import discord
from discord.ext import commands
import pokebase as pb
import random

class Pokedex(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["pokemon", "poke", "pk"], brief="Search up a Pokemon!", description="Get info about a random Pokemon or a specific Pokemon.", usage="`optional: Pokemon name`")
    async def pokedex(self, ctx, original_query = None):
        if isinstance(original_query, str):
            query = original_query.lower()
        else:
            query = original_query
        
        if query is None:
            query = random.randint(1, 1025)
        
        message = await ctx.reply("Fetching your Pokemon...")
        
        pokemon = pb.pokemon(query)
        
        '''
        try:
            pokemon.id
        except:
            tell the user something
            dont run the rest of the code
        '''
        
        try:
            id = pokemon.id
        except:
            await ctx.reply(f"`{original_query}` isn't a valid name or ID!")
            return

        
        name = pokemon.name.title()
        types = [item.type for item in pokemon.types]
        
        type_colors = {
            "normal": '#FFFFFF',
            "fire": '#EE8130',
            "water": '#6390F0',
            "electric": '#F7D02C',
            "grass": '#7AC74C',
            "ice": '#96D9D6',
            "fighting": '#C22E28',
            "poison": '#A33EA1',
            "ground": '#E2BF65',
            "flying": '#A98FF3',
            "psychic": '#F95587',
            "bug": '#A6B91A',
            "rock": '#B6A136',
            "ghost": '#735797',
            "dragon": '#6F35FC',
            "dark": '#705746',
            "steel": '#B7B7CE',
            "fairy": '#D685AD',
        }
        
        color = type_colors[types[0].name]
        
        height = pokemon.height / 10 # in meters
        weight = pokemon.weight / 10 # in kilograms
        abilities = [item.ability for item in pokemon.abilities]
        ability_names = [ability.name for ability in abilities]
        moves = [item.move for item in pokemon.moves]
        move_names = [move.name for move in moves]
        sprite = pb.SpriteResource("pokemon", id).url
        official_art = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png"

        species = pb.pokemon_species(name.lower()) 
        flavor_texts = species.flavor_text_entries
        
        english = next((item for item in flavor_texts if item.language.name == "en"), None)
        english_text = english.flavor_text.replace("\n", " ")
        version = str(english.version).title()
        
        link = f"https://bulbapedia.bulbagarden.net/wiki/{name}_(Pok%C3%A9mon)"
        
        
        embed = discord.Embed(
                title=f"#{id} | {name} ", 
                description=f"> **{english_text}** \n\- **{version}**\n\n**Type:** {", ".join([type.name.title() for type in types])}\n\n**Height:** {height}m **| Weight:** {weight}kg\n\n**Abilities:**\n{await self.bullet_list(ability_names)}\n\n[Click here for more info!]({link})",
                color = discord.Color.from_str(color),
            )
        
        embed.set_thumbnail(url=sprite)
        embed.set_image(url=official_art)
        embed.set_footer()
        
        await message.edit(embed=embed, content="Here you go!")

    
    async def bullet_list(self, list, title: bool=True, col: int=1):
        
        list_string = ""
        
        for i, item in enumerate(list):
            if title:
                item = item.title()
            
            list_string += f"• {item}"
            
            if i + 1 % col != 0:
                list_string += " "
            else:
                list_string += "\n"
                
        return list_string
        
    
async def setup(bot):
    await bot.add_cog(Pokedex(bot))