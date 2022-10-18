import datetime
from datetime import time
import requests
from discord.ext import commands, tasks

class Doll(commands.Cog):
    """Consulta o dolar a cada x tempo"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.dollar_to_real.start()


    @tasks.loop(hours=1)
    async def dollar_to_real(self):
        now = datetime.datetime.now()
        #NÃO RODA NOS FINAIS DE SEMANA!
        if ( now.weekday() != 5 and now.weekday() != 6):
            #RODA APENAS DE 9:00 AS 18 (GMT-3 & UTC−3)
            if ( now.hour <= 9 and now.hour >= 18):
                try:    
                    response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
                    data = response.json()
                    

                    cotacao_dolar = data["USDBRL"]["bid"]
                    
                    timeNow = now.strftime("%d/%m/%Y ás %H:%M:%S")

                    channel = self.bot.get_channel(1027341105123041280)
                    await channel.send(f"\n```━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n💸 Dólar : R${cotacao_dolar}\n\n📅 Em: {timeNow}  \n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n(próxima busca em 1 hora)\n```")
                

                except Exception as error:
                    await channel.send("Ops... Ocorreu algum problema na consulta )")
                    print(error)



def setup(bot):
    bot.add_cog(Doll(bot))
