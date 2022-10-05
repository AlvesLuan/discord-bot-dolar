import datetime
import requests
from discord.ext import commands, tasks

class Doll(commands.Cog):
    """Consulta o dolar a cada x tempo"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.dollar_to_real.start()

    @tasks.loop(minutes=5)
    async def dollar_to_real(self):
        try:    
            response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
            data = response.json()
            now = datetime.datetime.now()

            cotacao_dolar = data["USDBRL"]["bid"]
            
            timeNow = now.strftime("%d/%m/%Y ás %H:%M:%S")

            channel = self.bot.get_channel(1027341105123041280)
            await channel.send(f"\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n💸 Dólar : R${cotacao_dolar}\n\n📅 Em: {timeNow}  \n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n(próxima busca em 5 minuto)\n ")
            

        except Exception as error:
            await channel.send("Ops... Ocorreu algum problema na consulta )")
            print(error)



def setup(bot):
    bot.add_cog(Doll(bot))
