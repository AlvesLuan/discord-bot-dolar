from discord.ext import commands

class Talks(commands.Cog):
    """Conversa com o usuário"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="teste")
    async def test_bot(self, ctx):

        response = "Olá, Estou funcionando normalmente."

        await ctx.send(response)


def setup(bot):
    bot.add_cog(Talks(bot))
